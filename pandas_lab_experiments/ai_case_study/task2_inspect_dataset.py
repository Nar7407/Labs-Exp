import os
import pandas as pd

df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "patient_tests.csv"))

print("=" * 60)
print("DATASET INSPECTION")
print("=" * 60)

print(f"\n1. Number of rows and columns:")
print(f"   Shape: {df.shape}")
print(f"   Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print(f"\n2. Column names:")
print(f"   {list(df.columns)}")

print(f"\n3. Data types of each column:")
print(df.dtypes)

print(f"\n4. Basic statistical information (describe):")
print(df.describe())

print(f"\n5. Detailed info (info):")
df.info()
