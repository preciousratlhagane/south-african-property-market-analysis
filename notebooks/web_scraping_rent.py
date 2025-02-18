import csv
import os
import random
import time

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv


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

# Load enviromental_variables:
load_dotenv()
base_listing_url_for_rent = os.getenv("BASE_LISTING_URL_FOR_RENT")


def human_like_delay():
    base_delay = random.uniform(10, 20)
    jitter = random.uniform(-2, 2)  # Add some randomness
    time.sleep(base_delay + jitter)


# Create a function to extract a single listing url
property_url_response = requests.get("")
property_url_soup = BeautifulSoup(property_url_response.text, "html.parser")
listing_div = property_url_soup.find("div", class_="p24_regularTile")
print(listing_div)

# Extract the anchor tag and its href attribute
if listing_div:
    listing_link = listing_div.find("a", href=True)
    if listing_link:
        href = listing_link["href"]  # Extract the href
        print("Relative href:", href)
    else:
        print("No listing link found.")
else:
    print("No property listings found.")

# Create a function to extract the maximum number of pages
max_pages_response = requests.get("")
max_pages_soup = BeautifulSoup(max_pages_response.text, "html.parser")
pagination = max_pages_soup.find("ul", class_="pagination")
max_page_number = pagination.find_all("li")
max_page = int(max_page_number[-1].get_text(strip=True))
print(max_page)


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
