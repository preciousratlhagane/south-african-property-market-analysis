import csv
import os
import random
import time

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv


# Load enviromental_variables:
load_dotenv()
base_listing_url_for_rent = os.getenv("BASE_LISTING_URL_FOR_RENT")

# Generate a list of user agents
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.2420.81",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.4; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux i686; rv:124.0) Gecko/20100101 Firefox/124.0"
]

# Create a function to mimic human_like behaviour when scrolling on a website


def human_like_delay():
    base_delay = random.uniform(10, 20)
    jitter = random.uniform(-2, 2)  # Add some randomness
    time.sleep(base_delay + jitter)


# Create a function to determine the maximum pages of listings in each capital city
def get_max_num_of_pages(city_url):
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    human_like_delay()  # Pause between requests(changed)
    city_response = requests.get(city_url, headers=headers)

    if city_response.status_code != 200:
        print(f"Error accessing {city_url}, status: {
              city_response.status_code}")
        return 1

    soup = BeautifulSoup(city_response.text, "html.parser")

    pagination = soup.find("ul", class_="pagination")

    if not pagination:
        print("No pagination found, assuming 1 page")
        return 1

    # Find the last page number of the city listing
    max_page_number = pagination.find_all("li")

    if max_page_number:
        try:
            max_page = int(max_page_number[-1].get_text(strip=True))
            return max_page
        except ValueError:
            print("Could not determine max pages, defaulting to 1")
            return 1


# Intialize an empty dictionary to store the maximum number of pages of listings in each capital city
city_max_pages = {}

# Create a dictionary to store all the capital cities and their links:
capital_cities = {
    # "Johannesburg": "property-to-rent-in-johannesburg-c100",
    # "Bloemfontein": "property-to-rent-in-bloemfontein-c18",
    "Bhisho": "property-to-rent-in-bhisho-c247",
    # "Pietermaritzburg": "property-to-rent-in-pietermaritzburg-c147",
    # "Polokwane": "property-to-rent-in-polokwane-c703",
    # "Mbombela": "property-to-rent-in-mbombela-as170",
    # "Cape Town": "property-to-rent-in-cape-town-c432",
    # "Mafikeng": "property-to-rent-in-mafikeng-c133",
    # "Kimberley": "property-to-rent-in-kimberley-c715"
}


# Loop through the capital cities and store the maximum number of pages of listings in a dictionary
for city, slug in capital_cities.items():
    capital_city_url = f"{base_listing_url_for_rent}/{slug}"
    max_pages_per_city = get_max_num_of_pages(capital_city_url)
    city_max_pages[city] = max_pages_per_city
    print(f"{city}: {max_pages_per_city} found.")


# Create a function to extract the property_urls
def get_property_listing_urls(property_url):
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    page_listings = set()
    human_like_delay()
    listing_response = requests.get(property_url, headers=headers, timeout=15)

    if listing_response.status_code != 200:
        print(
            f"Error accessing {property_url}, status: {listing_response.status_code}")
        return []

    property_soup = BeautifulSoup(listing_response.text, "html.parser")
    listing_numbers = property_soup.find_all("div", class_="p24_regularTile")

    for ln in listing_numbers:
        links = ln.find_all("a")  # Ensure href exists
        for link in links:
            href = link.get("href")
            if href:
                page_listings.add(href)
                print(f"Found listing: {href}")

    return page_listings


# Initialise an empty dictionary to store the listing_urls
listing_urls = []


for city, pages in city_max_pages.items():
    # Get the correct slug for the city from capital_cities
    # Ensures city and slug are correctly matched
    slug = capital_cities.get(city)

    if not slug:
        print(f"Warning: No slug found for {city}, skipping...")
        continue  # Skip if no slug is found

    for page in range(1, pages + 1):
        print(f"Scraping page {page}/{pages} for {city}...")  # Show progress

        property_url = f"{base_listing_url_for_rent}/{slug}?Page={page}"
        page_listing_urls = get_property_listing_urls(property_url)

        # More efficient than using a loop
        listing_urls.extend(page_listing_urls)


# Create a function to extract the maximum number of pages
max_pages_response = requests.get("")
max_pages_soup = BeautifulSoup(max_pages_response.text, "html.parser")
pagination = max_pages_soup.find("ul", class_="pagination")
max_page_number = pagination.find_all("li")
max_page = int(max_page_number[-1].get_text(strip=True))
print(max_page)


response = requests.get("")
soup = BeautifulSoup(response.text, "html.parser")

title_div = soup.find("div", class_="sc_listingAddress")
title = title_div.find("h1")
final_result = title.get_text(strip=True)
print(final_result)

price = soup.find("div", class_="p24_mBM").text
print(price)


location = soup.select_one("div.p24_mBM p")
final_location = location.get_text(
    strip=True) if location else "Location not found."
print(final_location)

description = soup.find("div", class_="sc_listingDetailsText").text
print(description)

property_features = soup.find("div", id="accordion").text
print(property_features)
