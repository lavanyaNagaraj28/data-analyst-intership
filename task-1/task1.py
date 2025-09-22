import pandas as pd
import numpy as np
import re

# Load dataset
df = pd.read_csv("netflix_titles.csv")
print("Initial shape:", df.shape)

# Handle missing values
df['director'] = df['director'].fillna("Unknown Director")
df['cast'] = df['cast'].fillna("Unknown Cast")
df['country'] = df['country'].fillna("Unknown Country")

# Drop rows with missing critical fields
df = df.dropna(subset=['date_added', 'rating'])

# Remove duplicates
df.drop_duplicates(inplace=True)

# Clean text fields
df['type'] = df['type'].str.strip().str.title()
df['rating'] = df['rating'].str.strip()

# Convert dates
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year

# Clean column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Convert release_year to int
df['release_year'] = df['release_year'].astype(int)

# Extract numbers from duration
def extract_number(x):
    m = re.search(r'(\d+)', str(x))
    return int(m.group(1)) if m else np.nan

df['duration_num'] = df['duration'].apply(extract_number)

# Save cleaned dataset
df.to_csv("netflix_titles_cleaned.csv", index=False)

print("Cleaning completed. Saved as netflix_titles_cleaned.csv")
print("Final shape:", df.shape)
