"""Additional Question 2: Compare mean and median imputation"""

import os
import pandas as pd

df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ai_case_study", "patient_tests.csv"))

print("=" * 70)
print("Q2: MEAN vs MEDIAN IMPUTATION COMPARISON")
print("=" * 70)

glucose_mean = df["Glucose_Reading"].mean()
glucose_median = df["Glucose_Reading"].median()
glucose_std = df["Glucose_Reading"].std()

print(f"\nOriginal Glucose Statistics (excluding NaN):")
print(f"  Count: {df['Glucose_Reading'].count()}")
print(f"  Mean: {glucose_mean:.2f} mg/dL")
print(f"  Median: {glucose_median:.2f} mg/dL")
print(f"  Std Dev: {glucose_std:.2f} mg/dL")
print(f"  Mean-Median Difference: {abs(glucose_mean - glucose_median):.2f} mg/dL")

df_mean = df.copy()
df_median = df.copy()

df_mean["Glucose_Reading"] = df_mean["Glucose_Reading"].fillna(glucose_mean)
df_median["Glucose_Reading"] = df_median["Glucose_Reading"].fillna(glucose_median)

print("\n" + "-" * 70)
print("COMPARISON TABLE")
print("-" * 70)
print(f"{'Metric':<30} {'Mean Imp.':<15} {'Median Imp.':<15}")
print("-" * 70)
print(f"{'Imputed Value':<30} {glucose_mean:<15.2f} {glucose_median:<15.2f}")
print(f"{'Total Sum (mg/dL)':<30} {df_mean['Glucose_Reading'].sum():<15.2f} {df_median['Glucose_Reading'].sum():<15.2f}")
print(f"{'Overall Mean (mg/dL)':<30} {df_mean['Glucose_Reading'].mean():<15.2f} {df_median['Glucose_Reading'].mean():<15.2f}")
print(f"{'Overall Median (mg/dL)':<30} {df_mean['Glucose_Reading'].median():<15.2f} {df_median['Glucose_Reading'].median():<15.2f}")
print(f"{'Overall Std Dev':<30} {df_mean['Glucose_Reading'].std():<15.2f} {df_median['Glucose_Reading'].std():<15.2f}")
print("-" * 70)

print(f"\nImputed values for each patient:")
print(f"{'Patient_ID':<12} {'Original':<12} {'Mean Imp.':<12} {'Median Imp.':<12}")
print("-" * 50)
for idx, row in df.iterrows():
    orig = row["Glucose_Reading"]
    if pd.isna(orig):
        print(f"{row['Patient_ID']:<12} {'MISSING':<12} {glucose_mean:<12.2f} {glucose_median:<12.2f}")
    else:
        print(f"{row['Patient_ID']:<12} {orig:<12.2f} {'-':<12} {'-':<12}")

analysis = """
When to use MEAN imputation:
- Data is normally distributed (symmetric)
- No significant outliers
- Mean represents the "center" of the data well

When to use MEDIAN imputation:
- Data has outliers or is skewed
- Median is more robust to extreme values
- Better choice when outliers would skew the mean

In this dataset:
- If mean ≈ median (small difference), either works well
- If mean differs significantly from median, data may be skewed
- Median is generally safer when in doubt about distribution
"""
print("\n" + "=" * 70)
print("ANALYSIS")
print("=" * 70)
print(analysis)
