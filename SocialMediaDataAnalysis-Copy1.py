# ==============================
# Social Media Engagement Analysis
# ==============================

# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

# ----------------------------------
# Task 1: Generate Random Dataset
# ----------------------------------

# Define categories
categories = ['Food', 'Travel', 'Fashion', 'Fitness', 
              'Music', 'Culture', 'Family', 'Health']

# Number of records
n = 500

# Create dataset
data = {
    'Date': pd.date_range(start='2021-01-01', periods=n),
    'Category': [random.choice(categories) for _ in range(n)],
    'Likes': np.random.randint(0, 10000, size=n)
}

# Convert to DataFrame
df = pd.DataFrame(data)

print("\nFirst 5 Rows of Dataset:")
print(df.head())

# ----------------------------------
# Task 2: Data Exploration
# ----------------------------------

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

print("\nCategory Distribution:")
print(df['Category'].value_counts())

# ----------------------------------
# Task 3: Data Cleaning
# ----------------------------------

# Remove null values
df.dropna(inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Ensure correct data types
df['Date'] = pd.to_datetime(df['Date'])
df['Likes'] = df['Likes'].astype(int)

print("\nCleaned Dataset Info:")
df.info()

# ----------------------------------
# Task 4: Visualizations
# ----------------------------------
# 1️⃣ Histogram of Likes
plt.figure(figsize=(8, 5))
sns.histplot(df['Likes'], bins=30, kde=True)
plt.title('Distribution of Likes')
plt.xlabel('Number of Likes')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()

plt.savefig("histogram_likes.png")   # ← THIS SAVES THE IMAGE
plt.show()


# 2️⃣ Boxplot of Likes per Category
plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='Likes', data=df)
plt.title('Likes per Category')
plt.xlabel('Category')
plt.ylabel('Likes')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.savefig("boxplot_likes.png")   # ← THIS SAVES THE IMAGE
plt.show()


# ----------------------------------
# Task 5: Statistical Analysis
# ----------------------------------

# Overall Mean
mean_likes = df['Likes'].mean()
print(f"\nOverall Mean of Likes: {mean_likes:.2f}")

# Category-wise Mean
mean_likes_by_category = df.groupby('Category')['Likes'].mean()

print("\nMean Likes by Category:")
print(mean_likes_by_category)
