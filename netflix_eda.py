import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')

# Load dataset
df = pd.read_csv('netflix_titles.csv')

print("===== SHAPE =====")
print(df.shape, "\n")

print("===== INFO =====")
print(df.info(), "\n")

print("===== DESCRIBE =====")
print(df.describe(include='all'), "\n")

# Missing values
print("===== MISSING VALUES =====")
print(df.isnull().sum(), "\n")

plt.figure(figsize=(12,5))
sns.heatmap(df.isnull(), cbar=False)
plt.title('Missing Values Heatmap')
plt.show()

# Movies vs TV Shows
plt.figure(figsize=(6,4))
sns.countplot(x='type', data=df)
plt.title('Movies vs TV Shows')
plt.show()

# Ratings
plt.figure(figsize=(10,5))
sns.countplot(y='rating', data=df, order=df['rating'].value_counts().index)
plt.title('Ratings Distribution')
plt.show()

# Release Year Trend
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')
df['release_year'].value_counts().sort_index().plot(kind='line', figsize=(12,5))
plt.title('Titles Released Over Time')
plt.show()

# Genres
genres = df['listed_in'].str.split(',').explode().str.strip()
genres.value_counts().head(15).plot(kind='bar', figsize=(12,5))
plt.title('Top Genres')
plt.show()

# Countries
countries = df['country'].dropna().str.split(',').explode().str.strip()
countries.value_counts().head(15).plot(kind='bar', figsize=(12,5))
plt.title('Top Content-Producing Countries')
plt.show()

# Final Insights
print("===== FINAL INSIGHTS =====")
print("Movies vs Shows:\n", df['type'].value_counts(), "\n")
print("Top Genres:\n", genres.value_counts().head(10), "\n")
print("Top Countries:\n", countries.value_counts().head(10), "\n")
