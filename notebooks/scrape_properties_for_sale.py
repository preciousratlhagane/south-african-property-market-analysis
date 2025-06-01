import csv
import os
import random
import sys
import time

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

from src.config import USER_AGENTS

# Add the project root directory to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)


# Load enviromental_variables:
load_dotenv()
base_listing_url_for_rent = os.getenv("BASE_LISTING_URL_FOR_SALE")

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


a = get_property_features(
    "https://www.sahometraders.co.za/11-bedroom-house-for-sale-in-sterpark-111027045")
b = get_property_features(
    "https://www.sahometraders.co.za/4-bedroom-townhouse-for-sale-in-polokwane-central-116011363")
c = get_property_features(
    "https://www.sahometraders.co.za/3-bedroom-house-for-sale-in-polokwane-central-115965772")
d = get_property_features(
    "https://www.sahometraders.co.za/2-bedroom-townhouse-for-sale-in-bendor-115928367")
e = get_property_features(
    "https://www.sahometraders.co.za/vacant-land-plot-for-sale-in-mankweng-115992333")
f = get_property_features(
    "https://www.sahometraders.co.za/vacant-land-plot-for-sale-in-lebowakgomo-zone-a-115999124")
g = get_property_features(
    "https://www.sahometraders.co.za/3-bedroom-townhouse-for-sale-in-waterberry-country-estate-115991779")
h = get_property_features(
    "https://www.sahometraders.co.za/commercial-property-for-sale-in-bendor-116037272")
i = get_property_features(
    "https://www.sahometraders.co.za/5-bedroom-house-for-sale-in-sterpark-116037084")
j = get_property_features(
    "https://www.sahometraders.co.za/6-bedroom-house-for-sale-in-moregloed-115961074")
k = get_property_features(
    "https://www.sahometraders.co.za/3-bedroom-house-for-sale-in-polokwane-central-115837121")
l = get_property_features(
    "https://www.sahometraders.co.za/2-bedroom-townhouse-for-sale-in-polokwane-central-116002482")
m = get_property_features(
    "https://www.sahometraders.co.za/vacant-land-plot-for-sale-in-magna-via-industrial-116016454")
n = get_property_features(
    "https://www.sahometraders.co.za/4-bedroom-house-for-sale-in-polokwane-central-115964140")
o = get_property_features(
    "https://www.sahometraders.co.za/3-bedroom-house-for-sale-in-seshego-h-115978948")
p = get_property_features(
    "https://www.sahometraders.co.za/farm-for-sale-in-polokwane-rural-116012688")
q = get_property_features(
    "https://www.sahometraders.co.za/5-bedroom-house-for-sale-in-the-aloes-lifestyle-estate-115966562")
r = get_property_features(
    "https://www.sahometraders.co.za/7-bedroom-house-for-sale-in-polokwane-central-116038051")
s = get_property_features(
    "https://www.sahometraders.co.za/vacant-land-plot-for-sale-in-southern-gateway-115953231")
t = get_property_features(
    "https://www.sahometraders.co.za/4-bedroom-house-for-sale-in-sterpark-116006358")


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
    csv_filename = os.path.join(raw_folder, "polokwane_p1_purchases.csv")

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
