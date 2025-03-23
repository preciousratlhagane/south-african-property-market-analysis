# South African Property Market Analysis: Capital Cities

## 📌 Overview
This project analyzes real estate trends in South Africa's capital cities across all nine provinces. By examining rental and sale listings, we aim to uncover key market dynamics, affordability trends, and investment opportunities.


## 📊 Data Sources
The dataset consists of web-scraped property listings, capturing details such as: 
**Property Type** (Apartment, House, Townhouse, Farm etc.)
**Location** (Suburb, Province, Capital City)
**Price** (For Sale & Rent)
**Size** (Square meters, Number of bedrooms and bathrooms)
**Additional Features** (Garden, Garage, Pool, etc)


## 🎯 Objectives
**Compare** rental and sale prices across capital cities
**Identify** demand and supply trends in different cities
**Analyze** affordability and investment potential
**Evaluate** the impact of economic factors on property prices


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

## 🔍 Analysis Approach
**Data Collection**: Web scraping property listings using Python (i.e Beautiful Soup)
**Data Cleaning**: Handling missing values, creating new columns
**Exploratory Data Analysis**: Visualizing price distributions, market trends and city-wise comparisons
**Dashboard Creation**: Create a comprehensive dashboard on PowerBI

## Duplicating the .env File
To set up your environment variables, you need to duplicate the `.env.example` file and rename it to `.env`. You can do this manually or using the following terminal command:

```bash
cp .env.example .env # Linux, macOS, Git Bash, WSL
copy .env.example .env # Windows Command Prompt
```

This command creates a copy of `.env.example` and names it `.env`, allowing you to configure your environment variables specific to your setup.


## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── README.md          <- The top-level README for developers using this project
├── data
│   ├── external       <- Data from third party sources
│   ├── interim        <- Intermediate data that has been transformed
│   ├── processed      <- The final, canonical data sets for modeling
│   └── raw            <- The original, immutable data dump
│
├── models             <- Trained and serialized models, model predictions, or model summaries
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
    ├── features.py             <- Code to create features for modeling  
    │
    ├── plots.py                <- Code to create visualizations 
    │
    └── services                <- Service classes to connect with external platforms, tools, or APIs
        └── __init__.py 
```

--------