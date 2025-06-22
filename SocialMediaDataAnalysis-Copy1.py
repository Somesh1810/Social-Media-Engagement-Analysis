#!/usr/bin/env python
# coding: utf-8

# # Clean & Analyze Social Media

# ## Introduction
# 
# Social media has become a ubiquitous part of modern life, with platforms such as Instagram, Twitter, and Facebook serving as essential communication channels. Social media data sets are vast and complex, making analysis a challenging task for businesses and researchers alike. In this project, we explore a simulated social media, for example Tweets, data set to understand trends in likes across different categories.
# 
# ## Prerequisites
# 
# To follow along with this project, you should have a basic understanding of Python programming and data analysis concepts. In addition, you may want to use the following packages in your Python environment:
# 
# - pandas
# - Matplotlib
# - ...
# 
# These packages should already be installed in Coursera's Jupyter Notebook environment, however if you'd like to install additional packages that are not included in this environment or are working off platform you can install additional packages using `!pip install packagename` within a notebook cell such as:
# 
# - `!pip install pandas`
# - `!pip install matplotlib`
# 
# ## Project Scope
# 
# The objective of this project is to analyze tweets (or other social media data) and gain insights into user engagement. We will explore the data set using visualization techniques to understand the distribution of likes across different categories. Finally, we will analyze the data to draw conclusions about the most popular categories and the overall engagement on the platform.
# 
# ## Step 1: Importing Required Libraries
# 
# As the name suggests, the first step is to import all the necessary libraries that will be used in the project. In this case, we need pandas, numpy, matplotlib, seaborn, and random libraries.
# 
# Pandas is a library used for data manipulation and analysis. Numpy is a library used for numerical computations. Matplotlib is a library used for data visualization. Seaborn is a library used for statistical data visualization. Random is a library used to generate random numbers.

# In[14]:


# your code here
get_ipython().system('pip install pandas')
get_ipython().system('pip install matplotlib')


# In[16]:


# Task 1 – Import required libraries

import pandas as pd            # For creating and working with DataFrames
import numpy as np             # For numerical operations and random number generation
import matplotlib.pyplot as plt  # For displaying graphs and visualizations
import seaborn as sns          # For statistical data visualization
import random                  # For making random selections from lists


# In[18]:


# Task 2 – Generate random data for social media analysis

# Step 1: Define categories
categories = ['Food', 'Travel', 'Fashion', 'Fitness', 'Music', 'Culture', 'Family', 'Health']

# Step 2: Set the number of entries
n = 500

# Step 3: Create the data dictionary
data = {
    'Date': pd.date_range(start='2021-01-01', periods=n),  # Generates 500 sequential dates
    'Category': [random.choice(categories) for _ in range(n)],  # Randomly pick a category 500 times
    'Likes': np.random.randint(0, 10000, size=n)  # Generate 500 random likes between 0 and 9999
}

# Step 4: Convert to DataFrame
df = pd.DataFrame(data)

# Optional: Display first few rows
print(df.head())


# In[19]:


# Task 3 – Load the data into a Pandas DataFrame and Explore the Data

# Step 1: Load the data into a DataFrame (if not already done)
df = pd.DataFrame(data)

# Step 2: Print the first 5 rows of the DataFrame
print("First 5 rows of the dataset:")
print(df.head())

# Step 3: Print DataFrame information (data types, non-null counts, memory usage)
print("\nDataFrame Info:")
print(df.info())

# Step 4: Print a statistical summary of the numerical column(s)
print("\nDataFrame Description:")
print(df.describe())

# Step 5: Count of each category in the 'Category' column
print("\nCategory Value Counts:")
print(df['Category'].value_counts())


# In[20]:


# Task 4 – Clean the data

# Step 1: Remove any rows with null values
df = df.dropna()

# Step 2: Remove duplicate rows, if any
df = df.drop_duplicates()

# Step 3: Convert the 'Date' column to datetime format using pandas
df['Date'] = pd.to_datetime(df['Date'])

# Step 4: Convert 'Likes' column to integer (in case it's not already)
df['Likes'] = df['Likes'].astype(int)

# Step 5: Optional – Check the updated DataFrame structure
print("\nCleaned DataFrame Info:")
print(df.info())


# In[3]:


pip install --upgrade seaborn


# In[21]:


# Using distplot as a fallback for older seaborn versions
plt.figure(figsize=(8, 5))
sns.distplot(df['Likes'], bins=30, color='skyblue', kde=True, hist=True)
plt.title('Distribution of Likes')
plt.xlabel('Number of Likes')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()


# In[23]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

# Assuming you've already generated and cleaned `df` as per Tasks 2–4

# ----- Visualization -----

# 1. Histogram of Likes
plt.figure(figsize=(8, 5))
sns.distplot(df['Likes'], bins=30, kde=True, color='skyblue')
plt.title('Distribution of Likes')
plt.xlabel('Number of Likes')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Boxplot of Likes per Category
plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='Likes', data=df, palette='Set2')
plt.title('Likes per Category')
plt.xlabel('Category')
plt.ylabel('Likes')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# ----- Statistical Analysis -----

# 3. Overall Mean of Likes
mean_likes = df['Likes'].mean()
print(f"\nOverall Mean of Likes: {mean_likes:.2f}")

# 4. Mean Likes per Category
mean_likes_by_category = df.groupby('Category')['Likes'].mean()
print("\nMean Likes by Category:")
print(mean_likes_by_category)


# In[ ]:




