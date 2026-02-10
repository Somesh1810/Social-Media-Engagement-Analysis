#  Social Media Engagement Analysis  
### Exploratory Data Analysis & Visualization using Python

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)]
[![Pandas](https://img.shields.io/badge/Library-Pandas-blue)]
[![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-orange)]
[![Seaborn](https://img.shields.io/badge/Visualization-Seaborn-green)]
[![Status](https://img.shields.io/badge/Project-Completed-success)]

---

##  Project Summary

This project simulates and analyzes social media engagement data to identify patterns in user interactions across multiple content categories.

Using Python-based data analysis and visualization libraries, the project demonstrates a complete data pipeline:

- Data generation  
- Data cleaning  
- Exploratory Data Analysis (EDA)  
- Statistical analysis  
- Visualization-driven insights  

The analysis focuses on understanding how engagement (Likes) varies across different categories.

---

##  Objective

To analyze social media engagement trends by:

- Simulating structured engagement data
- Cleaning and preparing the dataset
- Visualizing Like distributions
- Identifying high-performing categories
- Computing statistical summaries

---

##  Dataset Overview

- **Total Records:** 500
- **Categories:** 8
    - Food
    - Travel
    - Fashion
    - Fitness
    - Music
    - Culture
    - Family
    - Health
- **Metrics Analyzed:** Likes
- **Date Range:** Starting from 2021-01-01

---

##  Data Processing Pipeline

###  Data Generation
- Random category assignment
- Random Like counts (0–10,000)
- Date range creation using `pd.date_range()`

###  Data Cleaning
- Removed null values
- Removed duplicates
- Converted Date to datetime format
- Ensured Likes were integer type

###  Exploratory Data Analysis
- Distribution analysis of Likes
- Category-wise comparison
- Statistical mean calculation

---

##  Visualizations

###  Histogram – Distribution of Likes
- Shows frequency distribution
- Identifies engagement spread
- Highlights skewness or outliers

###  Boxplot – Likes by Category
- Compares engagement across categories
- Detects high-performing content types
- Identifies variability and outliers

---

##  Statistical Analysis

- Calculated overall mean Likes
- Computed category-wise average Likes using `groupby()`

### Key Insight:
Categories such as **Fashion** and **Travel** showed higher average engagement, indicating stronger audience interaction compared to others.

---

##  Technology Stack

| Component | Tools Used |
|------------|------------|
| Programming | Python |
| Data Manipulation | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Statistical Analysis | Pandas GroupBy |

---

##  Project Structure
social-media-engagement-analysis/
│
├── analysis.py
├── histogram_likes.png
├── boxplot_likes.png
└── README.md


---

##  How to Run

###  Clone Repository

``
git clone https://github.com/Somesh1810/social-media-engagement-analysis.git
cd social-media-engagement-analysis ``

Install Dependencies
pip install pandas numpy matplotlib seaborn

Run Script
python analysis.py

Business Relevance

This project demonstrates practical skills required for:

Data Analyst roles

Marketing Analytics

Social Media Analytics

Business Intelligence

EDA & Visualization tasks

It simulates real-world engagement analysis used by digital marketing teams to:

Identify high-performing content

Optimize content strategies

Improve audience targeting

## Future Improvements

Time-series engagement trend analysis

Multi-metric analysis (Shares, Comments, Saves)

Predictive modeling for engagement forecasting

Dashboard creation using Power BI or Streamlit

Real-world dataset integration via APIs

 ## Academic Context

Course: Data Analytics / Python for Data Analysis
Institution: CHRIST (Deemed to be University), Bangalore
Author: Someshwar M
Generated on: 2025-06-22

## Author

Someshwar M
M.Sc. Data Analytics
Aspiring Data Analyst | Data Visualization Enthusiast

Mail:msomeshn@gmail.com
GitHub: https://github.com/Somesh1810
Linked In: www.linkedin.com/in/someshwar-m




