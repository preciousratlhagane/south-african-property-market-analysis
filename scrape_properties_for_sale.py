import csv
import os
import random
import time

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load enviromental_variables:
load_dotenv()
base_listing_url_for_rent = os.getenv("BASE_LISTING_URL_FOR_SALE")

# Define a list of user_agents to use while web scraping
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
    base_delay = random.uniform(3, 10)
    jitter = random.uniform(-1, 2)
    time.sleep(base_delay + jitter)


# Create a function to extract property features
def get_property_features(listing_url):
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


a = get_property_features("")
b = get_property_features("")
c = get_property_features("")
d = get_property_features("")
e = get_property_features("")
f = get_property_features("")
g = get_property_features("")
h = get_property_features("")
i = get_property_features("")
j = get_property_features("")
k = get_property_features("")
l = get_property_features("")
m = get_property_features("")
n = get_property_features("")
o = get_property_features("")
p = get_property_features("")
q = get_property_features("")
r = get_property_features("")
s = get_property_features("")
t = get_property_features("")


# List of dictionaries (property listings)
listings = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t]

# Ensure the list is not empty
if not listings:
    print("Error: No listings found.")
else:
    # Get the absolute path to the root of the project (one level up from "notebooks")
    project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))

    # Path to "data/interim"
    raw_folder = os.path.join(project_root, "data", "interim")

    # Ensure that the directory exists
    os.makedirs(raw_folder, exist_ok=True)

    # Save data to CSV
    csv_filename = os.path.join(raw_folder, "kimberley_p2_purchases.csv")

    # Extract field names from the first dictionary (assuming all have the same structure)
    fieldnames = listings[0].keys()

    # Write to CSV file
    with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header row
        writer.writeheader()

        # Write each dictionary as a row in the CSV
        writer.writerows(listings)

    print(
        f"CSV file '{csv_filename}' has been created successfully at {csv_filename}!")
