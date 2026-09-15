"""Additional Question 1: Median imputation for missing glucose values"""

import os
import pandas as pd

df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ai_case_study", "patient_tests.csv"))

print("=" * 60)
print("Q1: MEDIAN IMPUTATION FOR MISSING GLUCOSE VALUES")
print("=" * 60)

print(f"\nMissing glucose values before imputation: {df['Glucose_Reading'].isnull().sum()}")

glucose_median = df["Glucose_Reading"].median()
glucosemean = df["Glucose_Reading"].mean()

print(f"Median glucose reading: {glucose_median:.2f} mg/dL")
print(f"Mean glucose reading: {glucosemean:.2f} mg/dL")

df_median = df.copy()
df_median["Glucose_Reading"] = df_median["Glucose_Reading"].fillna(glucose_median)

print(f"\nMissing glucose values after median imputation: {df_median['Glucose_Reading'].isnull().sum()}")

print("\nComparison of original vs imputed values:")
print(df[["Patient_ID", "Glucose_Reading"]].to_string(index=False))
