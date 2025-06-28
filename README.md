# South African Property Market Analysis: Capital Cities

## Table of Contents

* [Overview](#overview)
* [Data Sources](#data-sources)
* [Objectives](#objectives)
* [Capital Cities Covered](#capital-cities-covered)
* [Project Pipeline](#project-pipeline)
* [Key Features of the Report](#key-features-of-the-report)
* [Technologies Used](#technologies-used)
* [Project Structure](#project-structure)
* [Getting Started](#getting-started)
* [Results and Insights](#results-and-insights)
* [Licence](#licence)


## 📌 Overview <a class="anchor" id="overview"></a>
Real estate investors aim to buy properties below market value and sell or rent them at competitive prices. Identifying such undervalued properties requires analysing a large volume of listing data, considering factors like location, size, amenities, market trends and price anomalies. 


## 📊 Data Sources <a class="anchor" id="data-sources"></a>
The dataset consists of web-scraped property listings, capturing details such as: 

- **Property Type** (Apartment, House, Townhouse, Farm, etc.)
- **Location** (Suburb, Province, Capital City)
- **Price** (For Sale & Rent)
- **Size** (Square meters, Number of bedrooms and bathrooms)
- **Additional Features** (Garden, Garage, Pool, etc)


## 🎯 Objectives <a class="anchor" id="objectives"></a>
- **Compare** rental and sale prices across capital cities
- **Identify** demand and supply trends in different cities
- **Analyse** affordability and investment potential
- **Evaluate** the impact of economic factors on property prices


## 🌆 Capital Cities Covered <a class="anchor" id="capital-cities-covered"></a>
| Province | Capital City |
|----------|-------------|
| Gauteng | Johannesburg |
| Western Cape | Cape Town |
| KwaZulu-Natal | Pietermaritzburg |
| Eastern Cape | Bhisho |
| Free State | Bloemfontein |
| Limpopo | Polokwane |
| Mpumalanga | Nelspruit |
| North West | Mafikeng |
| Northern Cape | Kimberley |


## 🪈 Project Pipeline <a class="anchor" id="project-pipeline"></a>

1. **Web Scraping** 
    - Tools: BeautifulSoup
    - Data Collected: Property type, price, suburb, city, size, features

2. **Data Cleaning and Preprocessing**
    - Removing duplicates, handling missing values
    - Extracting structured information from free-text fields
    - Standardising price and area formats

3. **Exploratory Data Analysis**
    - Removing duplicates and handling missing values
    - Extracting structured information from free-text fields
    - Standardising price, size, and categorical fields

4. **Data Export**
    - Clean dataset saved as `.csv` for easy import into Power BI

5. **PowerBI Report**
    - Interactive visuals including:
        - Price trends by city and suburb
        - Heatmaps for affordability and demand
        - Custom filters: location, property type, price range


## 📊 Key Features of the Report <a class="anchor" id="key-features-of-the-report"></a>

- Visual insights into market trends and outliers
- Geographic visualisations of affordability
- Compare prices by city and suburb
- Interactive filters for custom exploration


## 🖥️ Technologies Used: <a class="anchor" id="technologies-used"></a>
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-8A2BE2?style=for-the-badge) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![Power BI](https://img.shields.io/badge/Power%20BI-FAAB00?style=for-the-badge&logo=power%20bi&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=Tableau&logoColor=white)



## 📂 Project Structure <a class="anchor" id="project-structure"></a>

```
├── LICENSE            <- Open-source license if one is chosen
├── README.md          <- The top-level README for developers using this project
├── data
│   ├── interim        <- Intermediate data that has been transformed
│   ├── processed      <- The final, canonical data sets for modelling
│   └── raw            <- The original, immutable data dump
│
│
├── notebooks          <- Jupyter notebooks for data cleaning and exploration
│                         
│                         
│
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         Generated with `pip freeze > requirements.txt`
│
├── src                         <- Source code for this project
│    │
│    ├── __init__.py             <- Makes src a Python module
│    │
│    ├── config.py               <- Store useful variables and configuration
│    │
│    └── services                <- Service classes to connect with external platforms, tools, or APIs
│        └── __init__.py 
│
│
└── web_scraping
     ├── scrape_properties_for_sale.py
     └── scrape_rental_listings.py 
```

--------


## 🗄️ Getting Started <a class="anchor" id="getting-started"></a>

Explore this interactive South African property market dashboard to analyze listings, rentals vs. sales, trends by suburb and property type, and key real estate insights. x

To explore the insights:

1. **Download** the Power BI dashboard file located in the `dashboard/` folder:

```plaintext
reports/propertydashboard.pbix
```

2. **Open** the file using [Power BI Desktop](https://powerbi.microsoft.com/desktop/).

3. **Interact** with the visualisations:
    - Use slicers to filter by city, price range, property type, etc.
    - Hover over visuals to view tooltips and detailed stats
    - Explore maps and charts for geographic and trend-based insights


You can also view a similar interactive version on [Tableau Public](https://public.tableau.com/views/SouthAfricanPropertyDashboardAnalysis/SaleListings?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link) by clicking the link.

## 📈 Results and Insights <a class="anchor" id="results-and-insights"></a>


## 📜 Licence <a class="anchor" id="licence"></a>
This project is licensed under the MIT License – see the [LICENCE](./LICENCE) file for details.

> For educational and demonstration purposes. Data and visuals are not intended for commercial use.
