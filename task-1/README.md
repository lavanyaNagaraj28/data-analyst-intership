# Data Cleaning and Preprocessing – Task 1

## Dataset Used

Netflix Movies and TV Shows dataset from Kaggle.

## Steps Performed

1. **Handled Missing Values**

   * Filled missing `director` values with `"Unknown Director"`
   * Filled missing `cast` values with `"Unknown Cast"`
   * Filled missing `country` values with `"Unknown Country"`
   * Dropped rows with missing `date_added` or `rating`

2. **Removed Duplicates**

   * Used `drop_duplicates()` to remove duplicate records

3. **Standardized Text Columns**

   * Cleaned `type` column → ensured only `"Movie"` or `"Tv Show"`
   * Stripped extra spaces in `rating` values

4. **Date Handling**

   * Converted `date_added` column to datetime format
   * Extracted `year_added` column from `date_added`

5. **Renamed Columns**

   * Converted all column names to lowercase
   * Replaced spaces with underscores (e.g., `date_added`, `release_year`)

6. **Data Type Fixes**

   * Converted `release_year` to integer
   * Extracted numeric value from `duration` (e.g., `"90 min"` → `90`) into a new column `duration_num`

## Final Output

* Cleaned dataset saved as **`netflix_titles_cleaned.csv`**
* Dataset is free from duplicates, missing values are treated, columns are standardized, and ready for analysis.

## Repository Structure

```
DataCleaning_Task1/
│── netflix_titles.csv              # Raw dataset
│── clean_netflix.py                # Python script used for cleaning
│── netflix_titles_cleaned.csv      # Cleaned dataset
│── README.md                       # Summary report (this file)
```

---
