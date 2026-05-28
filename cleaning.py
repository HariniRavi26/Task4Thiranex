import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# LOAD DATASET
# -------------------------------

df = pd.read_csv("dataset.csv")

print("Dataset Loaded Successfully")

# -------------------------------
# SHOW FIRST ROWS
# -------------------------------

print(df.head())

# -------------------------------
# DATASET INFO
# -------------------------------

print(df.info())

# -------------------------------
# CHECK MISSING VALUES
# -------------------------------

print(df.isnull().sum())

# -------------------------------
# HANDLE MISSING VALUES
# -------------------------------

# Numerical columns
numeric_cols = df.select_dtypes(include='number').columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

# Text columns
text_cols = df.select_dtypes(include=['object', 'string']).columns

for col in text_cols:
    df[col] = df[col].fillna("Unknown")

print("Missing values handled successfully")

# -------------------------------
# REMOVE DUPLICATES
# -------------------------------

print("Duplicates Before:", df.duplicated().sum())

df = df.drop_duplicates()

print("Duplicates After:", df.duplicated().sum())

# -------------------------------
# CLEAN TEXT DATA
# -------------------------------

for col in text_cols:
    df[col] = df[col].str.strip()
    df[col] = df[col].str.title()

print("Text formatting cleaned")

# -------------------------------
# SAVE CLEANED DATA
# -------------------------------

df.to_csv("cleaned_data.csv", index=False)

print("Cleaned dataset saved successfully")

# -------------------------------
# SUMMARY REPORT
# -------------------------------

summary = df.describe(include='all')

summary.to_csv("summary_report.csv")

print("Summary report generated")

# -------------------------------
# CREATE CHARTS
# -------------------------------

for col in numeric_cols:

    plt.figure(figsize=(6,4))

    df[col].hist()

    plt.title(f"{col} Distribution")
    plt.xlabel(col)
    plt.ylabel("Count")

    plt.savefig(f"{col}_chart.png")

    plt.close()

print("Charts generated successfully")

# -------------------------------
# PROJECT COMPLETED
# -------------------------------

print("PROJECT COMPLETED SUCCESSFULLY")