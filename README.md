# 📊 Social Media Engagement Analysis

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas)
![Seaborn](https://img.shields.io/badge/Seaborn-0.13-4C72B0)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

An end-to-end **Exploratory Data Analysis (EDA)** project that simulates a real-world social media dataset and analyses user engagement across 8 content categories and 4 platforms — using Python, Pandas, Seaborn, and Matplotlib.

---

## 📌 Table of Contents
- [Problem Statement](#-problem-statement)
- [Dataset](#-dataset)
- [Project Pipeline](#-project-pipeline)
- [Key Findings](#-key-findings)
- [Visualisations](#-visualisations)
- [Tech Stack](#-tech-stack)
- [How to Run](#-how-to-run)
- [Project Structure](#-project-structure)
- [Future Improvements](#-future-improvements)

---

## 🎯 Problem Statement

Social media managers and content strategists need to understand **which content categories and platforms drive the highest user engagement**. This project simulates 500 posts over 16 months and answers:

- Which content category has the highest engagement rate?
- Which platform performs best?
- How does engagement trend over time?
- Which metrics are most correlated with high engagement?

---

## 📂 Dataset

| Column | Type | Description |
|---|---|---|
| `Date` | datetime | Post date (Jan 2023 – May 2024) |
| `Category` | str | Content category (Food, Travel, Fashion, etc.) |
| `Platform` | str | Instagram, Twitter, Facebook, TikTok |
| `Views` | int | Total post views |
| `Likes` | int | Total likes |
| `Comments` | int | Total comments |
| `Shares` | int | Total shares |
| `total_engagement` | int | Likes + Comments + Shares *(engineered)* |
| `engagement_rate` | float | (total_engagement / Views) × 100 *(engineered)* |

- **500 records** · **No null values** · **No duplicates**
- Likes, Comments, and Shares are generated as realistic proportions of Views

---

## 🔄 Project Pipeline

```
Generate Dataset → Explore → Clean → Feature Engineering → Analyse → Visualise → Insights
```

| Step | Task |
|---|---|
| 1 | Generate multi-column simulated dataset with realistic ratios |
| 2 | Data exploration — dtypes, nulls, distributions, value counts |
| 3 | Data cleaning — drop nulls, duplicates, enforce types |
| 4 | Feature engineering — engagement_rate, total_engagement, YearMonth |
| 5 | Statistical analysis — category/platform averages, top 10 posts, correlation matrix |
| 6 | 7 visualisations saved as high-res PNGs |
| 7 | Automated key insights summary printed to console |

---

## 📈 Key Findings

| Metric | Result |
|---|---|
| Overall avg engagement rate | **40.17%** |
| Highest engagement category | **Fashion (43.33%)** |
| Lowest engagement category | **Family (35.59%)** |
| Best performing platform | **Twitter (42.13%)** |
| Strongest metric correlation | **Likes ↔ Total Engagement (r = 0.98)** |
| Engagement rate vs Views | **No correlation (r = −0.01)** — more views does not mean better engagement rate |

> 💡 **Key insight:** A post going viral (high Views) does not guarantee a high engagement rate. Content quality (Likes, Comments, Shares relative to Views) matters more than raw reach.

---

## 📊 Visualisations

| # | Chart | Insight |
|---|---|---|
| 1 | Histogram of Likes | Roughly uniform distribution across 0–30K likes |
| 2 | Boxplot — Likes by Category | Fashion and Travel show higher median likes |
| 3 | Avg Engagement Rate by Category | Fashion leads at 43.33%; Family lags at 35.59% |
| 4 | Monthly Engagement Trend | Engagement peaks visible in mid and end-of-year months |
| 5 | Avg Engagement Rate by Platform | Twitter slightly outperforms TikTok |
| 6 | Correlation Heatmap | Likes strongly predict total engagement (r = 0.98) |
| 7 | Likes vs Views Scatter | Positive trend with category-level variation |

> Charts are saved to the `charts/` folder after running the script.

---

## 🛠 Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10+ | Core language |
| Pandas | Data manipulation and groupby analysis |
| NumPy | Random data generation and numerical ops |
| Matplotlib | Base plotting and chart customisation |
| Seaborn | Statistical visualisations |

---

## ▶️ How to Run

**1. Clone the repository**
```bash
git clone https://github.com/Somesh1810/Social-Media-Engagement-Analysis.git
cd Social-Media-Engagement-Analysis
```

**2. Install dependencies**
```bash
pip install pandas numpy matplotlib seaborn
```

**3. Run the script**
```bash
python3 SocialMediaDataAnalysis.py
```

Charts will be saved automatically to the `charts/` folder.

---

## 🗂 Project Structure

```
Social-Media-Engagement-Analysis/
│
├── SocialMediaDataAnalysis.py   # Main analysis script
├── charts/                      # Output visualisations (auto-created)
│   ├── 01_histogram_likes.png
│   ├── 02_boxplot_likes_category.png
│   ├── 03_engagement_rate_category.png
│   ├── 04_monthly_trend.png
│   ├── 05_engagement_rate_platform.png
│   ├── 06_correlation_heatmap.png
│   └── 07_scatter_likes_views.png
├── Social_Media_Engagement_Analysis.pdf   # Project report
└── README.md
```

---

## 🚀 Future Improvements

- [ ] Use a real dataset from Kaggle (e.g. Instagram/Twitter engagement data)
- [ ] Add a Jupyter Notebook version with inline charts
- [ ] Build an interactive Streamlit dashboard
- [ ] Extend to multi-year trend analysis
- [ ] Add a simple ML model to predict engagement rate

---

## 👤 Author

**Somesh** · [GitHub @Somesh1810](https://github.com/Somesh1810)

*Built as part of a data analyst portfolio project.*
