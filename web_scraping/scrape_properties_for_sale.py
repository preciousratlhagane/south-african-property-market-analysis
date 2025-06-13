import csv
import os
import random
import sys
import time

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Add the project root directory to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

from src.config import USER_AGENTS  # noqa: E402

# Load enviromental_variables:
load_dotenv()
base_listing_url_for_sale = os.getenv("BASE_LISTING_URL_FOR_SALE")


def human_like_delay():
    """
    Introduces a randomized delay to simulate human-like behaviour.

    The function pauses the program execution or a duration composed of:
    - A base delay randomly selected between 3 and 10 seconds
    - An additional jitter randomly selected between -1 and 2 seconds
    """
    base_delay = random.uniform(3, 10)
    jitter = random.uniform(-1, 2)
    time.sleep(base_delay + jitter)


def get_max_num_of_pages(city_url):
    """
    Determinees the maximum number of pages avaliable for a given city's listing URL

    This function sends an HTTP GET request to the specified `city_url`, simulating human-like behaviour with a randomized delay and rotating user-agent headers.
    It then parses the pagination section of the HTML response to extract the maximum number of avaliable pages for listings in that city.

    Args:
        city_url (str): The URL of the city-specific listings page.

    Returns:
        int: The maximum number of pagination pages. Returns 1 if the page fails to load, if pagination is not found, or if the page number cannot be parsed. 
    """
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    human_like_delay()
    city_response = requests.get(city_url, headers=headers)

    if city_response.status_code != 200:
        print(
            f"Error accessing {city_url}, status: {city_response.status_code}")
        return 1

    soup = BeautifulSoup(city_response.text, "html_parser")

    pagination = soup.find("ul", class_="pagination")

    if not pagination:
        print("No pagination found, assuming 1 page")

    max_page_number = pagination.find_all("li")

    if max_page_number:
        try:
            max_page = int(max_page_number[-1].get_text(strip=True))
            return max_page
        except ValueError:
            print("Could not determine max pages, defaulting to 1")
            return 1


# Initialize an empty dictionary to store the maximum number of pages of listings in each capital city
city_max_pages = {}

# Create a dictionary to store all the capital cities and their links:
capital_cities = {
    "Johannesburg": "property-for-sale-in-johannesburg-c100",
    "Bloemfontein": "property-for-sale-in-bloemfontein-c18",
    "Bhisho": "property-for-sale-in-bhisho-c247",
    "Pietermaritzburg": "property-for-sale-in-pietermaritzburg-c147",
    "Polokwane": "property-for-sale-in-polokwane-c703",
    "Mbombela": "property-for-sale-in-mbombela-as170",
    "Cape Town": "property-for-sale-in-cape-town-c432",
    "Mafikeng": "property-for-sale-in-mafikeng-c133",
    "Kimberley": "property-for-sale-in-kimberley-c715"
}

# Loop through the capital cities and store the maximum number of pages of listings in a dictionary
for city, slug in capital_cities.items():
    capital_city_url = f"{base_listing_url_for_sale}/{slug}"
    max_pages_per_city = get_max_num_of_pages(capital_city_url)
    city_max_pages[city] = max_pages_per_city
    print(f"{city}: {max_pages_per_city} found")


def get_property_listing_urls(property_url):
    """
    Extracts individual property listing URLs from a given property listings page.

    This function sends a GET request to the provided `property_url`, simulating human-like browsing behaviour with randomized delays and user-agent headers. 
    It parses the HTML content to find all anchor tags within listing tiles and extract valid `href` attributes pointing to individual listings

    Args:
        property_url (str): The URL of the main property listings page

    Returns:
        set: A set of strings, each representing a relative URL to an individual property listing. Returns an empty set if the request fails or no listings are found. 
    """
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    page_listings = set()
    human_like_delay()
    listing_response = requests.get(property_url, headers=headers, timeout=15)

    if listing_response.status_code != 200:
        print(
            f"Error accessing {property_url}, status: {listing_response.status_code}")
        return set()

    property_soup = BeautifulSoup(listing_response.text, "html_parser")
    listing_numbers = property_soup.find_all("div", class_="p24_regularTile")

    for ln in listing_numbers:
        links = ln.find_all("a")
        for link in links:
            href = link.get("href")
            if href:
                page_listings.add(href)
                print(f"Found listing: {href}")

    return page_listings


# Intialise an empty list to store the listing urls
listing_urls = []

# Iterate and store the property_listing urls
for city, pages in city_max_pages.items():

    # Get the correctly matched slug for each city
    slug = capital_cities.get(city)

    if not slug:
        print(f"Warning: No slug found for {city}, skipping...")
        continue

    for page in range(1, pages + 1):
        print(f"Scraping page {page}/{pages} for {city}...")

        property_url = f"{base_listing_url_for_sale}/{slug}?Page={page}"
        page_listing_urls = get_property_listing_urls(property_url)

        # Store the information in a list
        listing_urls.extend(page_listing_urls)


def get_property_features(listing_url):
    """
    Extracts property details from an individual property listing URL

    This function simulates human-like browsing by adding a randomized delay and rotating user-agent headers. It sends a GET request to the specified listing URL and parses the HTML response to extract key property information such as price, location, title, description, and features.

    Args:
        listing_url (str): The URL of the property listing page.

    Returns:
        dict: A dictionary containing extracted property listing details:
            - 'url': The original listing URL.
            - 'price': The price of the property (string or "N/A").
            - 'location': The property's location (string or "N/A").
            - 'property_title': The title/header of the listing (string or "N/A").
            - 'property descripttion: The main description of the listing (string or "N/A").
            - 'property_features': Additional features listed on the page (string or "N/A").

        Returns None if the request fails or the page returns a non-200 status code.
    """
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    human_like_delay()  # Ensure this function is defined

    try:
        listing_response = requests.get(
            listing_url, headers=headers, timeout=15)

        if listing_response.status_code != 200:
            print(
                f"Error accessing {listing_url}, status: {listing_response.status_code}")
            return None  # Return None for consistency

        listing_soup = BeautifulSoup(listing_response.text, "html.parser")

        # Get the price of a property listing
        price = listing_soup.find("div", class_="p24_mBM")
        price = price.get_text(strip=True) if price else "N/A"

        # Get the location of a property listing
        location_div = listing_soup.select_one("div.p24_mBM p")
        location = location_div.get_text(strip=True) if location_div else "N/A"

        # Get the title of the listing
        title_div = listing_soup.find("div", class_="sc_listingAddress")
        property_title = title_div.find("h1").get_text(
            strip=True) if title_div else "N/A"

        # Get the property description
        description_div = listing_soup.find(
            "div", class_="sc_listingDetailsText")
        property_description = description_div.get_text(
            strip=True) if description_div else "N/A"

        # Get the property features
        features_div = listing_soup.find("div", id="accordion")
        property_features = features_div.get_text(
            strip=True) if features_div else "N/A"

        return {
            "url": listing_url,
            "price": price,
            "location": location,
            "property_title": property_title,
            "property_description": property_description,
            "property_features": property_features,
        }

    except requests.RequestException as e:
        print(f"Request failed for {listing_url}: {e}")
        return None


# Create an empty list to store scrapped property data
property_data_list = []

# Iterate through the property_urls and store the information in a list
for urls in listing_urls:
    property_listing_url = f"{base_listing_url_for_sale}/{urls}"
    property_info = get_property_features(property_listing_url)

    if property_info:
        property_data_list.append(property_info)

# Get the absolute path to the root of the project
project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))

raw_folder = os.path.join(project_root, "data", "raw")

# Ensure that the directory exists
os.makedirs(raw_folder, exist_ok=True)

# Save data to CSV file
csv_filename = os.path.join(
    raw_folder, "listings_for_sale_in_capital_cities.csv")

# Define CSV column headers
csv_columns = ["url", "price", "location", "property_title",
               "property_description", "property_features"]

# Write to CSV file
with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=csv_columns)

    writer.writeheader()
    writer.writerows(property_data_list)

print(f"Data successfully saved to {csv_filename}")
