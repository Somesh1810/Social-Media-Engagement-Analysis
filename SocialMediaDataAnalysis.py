# ============================================================
# Social Media Engagement Analysis — Upgraded Version
# Author: [Your Name]
# Tools: Python, Pandas, NumPy, Matplotlib, Seaborn
# Description: End-to-end EDA pipeline on a simulated social
#              media dataset with engagement metrics, trend
#              analysis, correlation study, and visualisations.
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import random
import os

# ── Output folder ────────────────────────────────────────────
OUTPUT_DIR = "charts"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Plot style ───────────────────────────────────────────────
sns.set_theme(style="whitegrid", palette="Set2")
plt.rcParams.update({
    "figure.dpi": 150,
    "axes.titlesize": 14,
    "axes.labelsize": 12,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
})


# ============================================================
# STEP 1 — Generate Richer Dataset
# ============================================================

def generate_dataset(n: int = 500, seed: int = 42) -> pd.DataFrame:
    """
    Generate a simulated social media dataset.

    Parameters
    ----------
    n    : Number of records
    seed : Random seed for reproducibility

    Returns
    -------
    pd.DataFrame with columns:
        Date, Category, Platform, Likes, Comments, Shares, Views
    """
    np.random.seed(seed)
    random.seed(seed)

    categories = ["Food", "Travel", "Fashion", "Fitness",
                  "Music", "Culture", "Family", "Health"]
    platforms  = ["Instagram", "Twitter", "Facebook", "TikTok"]

    views    = np.random.randint(500,  50_000, size=n)
    likes    = (views * np.random.uniform(0.01, 0.60, size=n)).astype(int)
    comments = (views * np.random.uniform(0.00, 0.10, size=n)).astype(int)
    shares   = (views * np.random.uniform(0.00, 0.08, size=n)).astype(int)

    data = {
        "Date"    : pd.date_range(start="2023-01-01", periods=n, freq="D"),
        "Category": [random.choice(categories) for _ in range(n)],
        "Platform": [random.choice(platforms)   for _ in range(n)],
        "Views"   : views,
        "Likes"   : likes,
        "Comments": comments,
        "Shares"  : shares,
    }
    return pd.DataFrame(data)


df_raw = generate_dataset(n=500)

print("=" * 55)
print("STEP 1 — Raw Dataset")
print("=" * 55)
print(df_raw.head())
print(f"\nShape: {df_raw.shape}")


# ============================================================
# STEP 2 — Data Exploration
# ============================================================

print("\n" + "=" * 55)
print("STEP 2 — Exploration")
print("=" * 55)
print("\nData types:\n", df_raw.dtypes)
print("\nNull values:\n", df_raw.isnull().sum())
print("\nStatistical summary:\n", df_raw.describe())
print("\nCategory counts:\n", df_raw["Category"].value_counts())
print("\nPlatform counts:\n",  df_raw["Platform"].value_counts())


# ============================================================
# STEP 3 — Data Cleaning
# ============================================================

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the dataset:
    - Drop nulls and duplicates
    - Enforce correct data types
    - Remove rows where Views == 0 (avoids division by zero)
    """
    df = df.dropna().drop_duplicates().copy()
    df["Date"]     = pd.to_datetime(df["Date"])
    df["Views"]    = df["Views"].astype(int)
    df["Likes"]    = df["Likes"].astype(int)
    df["Comments"] = df["Comments"].astype(int)
    df["Shares"]   = df["Shares"].astype(int)
    df = df[df["Views"] > 0]
    return df


df = clean_data(df_raw)

print("\n" + "=" * 55)
print("STEP 3 — Cleaned Dataset")
print("=" * 55)
df.info()
print(f"\nRecords after cleaning: {len(df)}")


# ============================================================
# STEP 4 — Feature Engineering
# ============================================================

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add derived columns:
    - engagement_rate : (Likes + Comments + Shares) / Views * 100
    - total_engagement: Likes + Comments + Shares
    - Month            : calendar month label
    - YearMonth        : period for trend grouping
    """
    df = df.copy()
    df["total_engagement"] = df["Likes"] + df["Comments"] + df["Shares"]
    df["engagement_rate"]  = (df["total_engagement"] / df["Views"] * 100).round(2)
    df["Month"]            = df["Date"].dt.strftime("%b")
    df["YearMonth"]        = df["Date"].dt.to_period("M")
    return df


df = engineer_features(df)

print("\n" + "=" * 55)
print("STEP 4 — Feature Engineering")
print("=" * 55)
print(df[["Date", "Category", "Platform",
          "total_engagement", "engagement_rate"]].head(10))


# ============================================================
# STEP 5 — Statistical Analysis
# ============================================================

print("\n" + "=" * 55)
print("STEP 5 — Statistical Analysis")
print("=" * 55)

# 5a. Overall engagement stats
print("\nOverall Engagement Rate (%):")
print(df["engagement_rate"].describe().round(2))

# 5b. Average engagement rate by category
cat_stats = (df.groupby("Category")["engagement_rate"]
               .mean()
               .sort_values(ascending=False)
               .round(2))
print("\nAvg Engagement Rate by Category (%):\n", cat_stats)

# 5c. Average engagement rate by platform
plat_stats = (df.groupby("Platform")["engagement_rate"]
                .mean()
                .sort_values(ascending=False)
                .round(2))
print("\nAvg Engagement Rate by Platform (%):\n", plat_stats)

# 5d. Top 10 posts
top10 = (df.nlargest(10, "total_engagement")
           [["Date","Category","Platform","Views",
             "total_engagement","engagement_rate"]])
print("\nTop 10 Posts by Total Engagement:\n", top10.to_string(index=False))

# 5e. Correlation matrix
numeric_cols = ["Views", "Likes", "Comments", "Shares",
                "total_engagement", "engagement_rate"]
corr_matrix = df[numeric_cols].corr().round(2)
print("\nCorrelation Matrix:\n", corr_matrix)


# ============================================================
# STEP 6 — Visualisations
# ============================================================

def save(fig, name: str) -> None:
    path = os.path.join(OUTPUT_DIR, name)
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"  ✓ Saved → {path}")


print("\n" + "=" * 55)
print("STEP 6 — Saving Visualisations")
print("=" * 55)

# ── Chart 1: Distribution of Likes (FIX #1 — histplot not distplot) ──
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df["Likes"], bins=30, kde=True, ax=ax, color="#4C72B0")
ax.set_title("Distribution of Likes")
ax.set_xlabel("Number of Likes")
ax.set_ylabel("Frequency")
save(fig, "01_histogram_likes.png")

# ── Chart 2: Boxplot — Likes per Category ────────────────────
fig, ax = plt.subplots(figsize=(10, 6))
order = df.groupby("Category")["Likes"].median().sort_values(ascending=False).index
sns.boxplot(x="Category", y="Likes", data=df, order=order,
            hue="Category", palette="Set2", legend=False, ax=ax)
ax.set_title("Likes per Category")
ax.set_xlabel("Category")
ax.set_ylabel("Likes")
ax.tick_params(axis="x", rotation=45)
save(fig, "02_boxplot_likes_category.png")

# ── Chart 3: Avg Engagement Rate by Category (bar chart) ─────
fig, ax = plt.subplots(figsize=(9, 6))
cat_stats.sort_values().plot(kind="barh", color=sns.color_palette("Set2"), ax=ax)
ax.set_title("Average Engagement Rate by Category (%)")
ax.set_xlabel("Engagement Rate (%)")
ax.set_ylabel("Category")
ax.xaxis.set_major_formatter(mticker.FormatStrFormatter("%.1f%%"))
save(fig, "03_engagement_rate_category.png")

# ── Chart 4: Monthly Trend — Total Engagement ────────────────
monthly = (df.groupby("YearMonth")["total_engagement"]
             .sum()
             .reset_index())
monthly["YearMonth"] = monthly["YearMonth"].astype(str)

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(monthly["YearMonth"], monthly["total_engagement"],
        marker="o", linewidth=2, color="#55A868")
ax.fill_between(monthly["YearMonth"], monthly["total_engagement"],
                alpha=0.15, color="#55A868")
ax.set_title("Monthly Total Engagement Trend")
ax.set_xlabel("Month")
ax.set_ylabel("Total Engagement")
step = max(1, len(monthly) // 12)
ax.set_xticks(range(0, len(monthly), step))
ax.set_xticklabels(monthly["YearMonth"].iloc[::step], rotation=45, ha="right")
save(fig, "04_monthly_trend.png")

# ── Chart 5: Avg Engagement Rate by Platform ─────────────────
fig, ax = plt.subplots(figsize=(7, 5))
plat_stats.plot(kind="bar", color=sns.color_palette("pastel"), ax=ax, edgecolor="grey")
ax.set_title("Average Engagement Rate by Platform (%)")
ax.set_xlabel("Platform")
ax.set_ylabel("Engagement Rate (%)")
ax.tick_params(axis="x", rotation=30)
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.1f%%"))
for bar in ax.patches:
    ax.annotate(f"{bar.get_height():.2f}%",
                (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                ha="center", va="bottom", fontsize=9)
save(fig, "05_engagement_rate_platform.png")

# ── Chart 6: Correlation Heatmap ─────────────────────────────
fig, ax = plt.subplots(figsize=(8, 6))
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm",
            mask=mask, linewidths=0.5, ax=ax,
            vmin=-1, vmax=1, cbar_kws={"shrink": 0.8})
ax.set_title("Correlation Heatmap of Engagement Metrics")
save(fig, "06_correlation_heatmap.png")

# ── Chart 7: Likes vs Views (scatter, coloured by category) ──
fig, ax = plt.subplots(figsize=(9, 6))
categories = df["Category"].unique()
palette = sns.color_palette("Set2", n_colors=len(categories))
for cat, color in zip(categories, palette):
    subset = df[df["Category"] == cat]
    ax.scatter(subset["Views"], subset["Likes"],
               alpha=0.5, label=cat, color=color, s=20)
ax.set_title("Likes vs Views by Category")
ax.set_xlabel("Views")
ax.set_ylabel("Likes")
ax.legend(title="Category", bbox_to_anchor=(1.01, 1), loc="upper left", fontsize=9)
save(fig, "07_scatter_likes_views.png")


# ============================================================
# STEP 7 — Key Insights Summary
# ============================================================

print("\n" + "=" * 55)
print("STEP 7 — Key Insights")
print("=" * 55)

best_cat  = cat_stats.idxmax()
worst_cat = cat_stats.idxmin()
best_plat = plat_stats.idxmax()

print(f"\n• Highest avg engagement category : {best_cat}  ({cat_stats[best_cat]:.2f}%)")
print(f"• Lowest  avg engagement category : {worst_cat} ({cat_stats[worst_cat]:.2f}%)")
print(f"• Best performing platform        : {best_plat} ({plat_stats[best_plat]:.2f}%)")
print(f"• Overall avg engagement rate     : {df['engagement_rate'].mean():.2f}%")
print(f"• Total records analysed          : {len(df)}")
print(f"\nAll charts saved to ./{OUTPUT_DIR}/")
print("\nPipeline complete ✓")