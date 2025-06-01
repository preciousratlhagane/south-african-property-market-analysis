# South African Property Market Analysis: Capital Cities


## 📌 Overview
Real estate investors aim to buy properties below market value and sell or rent them at competitive prices. The process of identifying such undervalued properties requires analyzing a large volume of listing data, considering factors like location, size, amenities, market trends and price anomalies. 


## 📊 Data Sources
The dataset consists of web-scraped property listings, capturing details such as: 
- **Property Type** (Apartment, House, Townhouse, Farm etc.)
- **Location** (Suburb, Province, Capital City)
- **Price** (For Sale & Rent)
- **Size** (Square meters, Number of bedrooms and bathrooms)
- **Additional Features** (Garden, Garage, Pool, etc)


## 🎯 Objectives
- **Compare** rental and sale prices across capital cities
- **Identify** demand and supply trends in different cities
- **Analyze** affordability and investment potential
- **Evaluate** the impact of economic factors on property prices


## 🌆 Capital Cities Covered 
| Province | Capital City |
|----------|-------------|
| Gauteng | Johannesburg |
| Western Cape | Cape Town |
| KwaZulu-Natal | Pietermaritzburg |
| Eastern Cape | Bhisho |
| Free State | Bloemfontein |
| Limpopo | Polokwane |
| Mpumalanga | Mbombela |
| North West | Mahikeng |
| Northern Cape | Kimberley |


## 🪈 Project Pipeline

1. **Web Scraping** 
    - Tools: 
    - Data Collected: 

2. **Data Cleaning and Preprocessing**
    - Removing duplicatess, handling missing values
    - Extracting structured information from free-text fields
    - Standardizing price and area formats

3. **Exploratory Data Analysis**
    -
    -
    -

4. **Data Export**
    - Clean dataset saved as `.csv` for easy import into Power BI

5. **PowerBI Dashboard**
    - Interactive visuals including:
        - Price trends by city and suburb
        - 
        - 

## 📊 Key Features of the Dashboard

## 🖥️ Technologies Used: 
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-8A2BE2?style=for-the-badge) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![Power BI](https://img.shields.io/badge/Power%20BI-FAAB00?style=for-the-badge&logo=power%20bi&logoColor=white) 



## 📂 Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── README.md          <- The top-level README for developers using this project
├── dashboard
│   ├── propertydashboard.pbix   <- PowerBI dashboard file
├── data
│   ├── interim        <- Intermediate data that has been transformed
│   ├── processed      <- The final, canonical data sets for modeling
│   └── raw            <- The original, immutable data dump
│
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
└── src                         <- Source code for this project
    │
    ├── __init__.py             <- Makes src a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── plots.py                <- Code to create visualizations 
    │
    └── services                <- Service classes to connect with external platforms, tools, or APIs
        └── __init__.py 
```

--------