"""AI Case Study: Patient Test-Result Analysis using Pandas DataFrame - Task 3"""

import os
import pandas as pd

df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "patient_tests.csv"))

print("=" * 60)
print("MISSING VALUES ANALYSIS")
print("=" * 60)

missing_counts = df.isnull().sum()

print("\nNumber of missing values in each column:")
print(missing_counts)

print("\nColumns with missing values:")
for col in df.columns:
    if missing_counts[col] > 0:
        print(f"  - {col}: {missing_counts[col]} missing values")

print(f"\nTotal missing values in dataset: {missing_counts.sum()}")

print(f"\nFocusing on Glucose_Reading column:")
print(f"  Missing values: {df['Glucose_Reading'].isnull().sum()}")
print(f"  Total records: {len(df)}")
print(f"  Available readings: {df['Glucose_Reading'].notnull().sum()}")
print(f"  Percentage missing: {(df['Glucose_Reading'].isnull().sum() / len(df)) * 100:.2f}%")
