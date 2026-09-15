import os
import pandas as pd

df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ai_case_study", "patient_tests.csv"))

print("=" * 70)
print("Q9: CREATE NEW DATAFRAME WITH SPECIFIC COLUMNS")
print("=" * 70)

print("\nOriginal DataFrame columns:")
print(list(df.columns))

new_df_1 = df[["Patient_ID", "Ward", "Glucose_Reading", "Turnaround_Time"]]
print("\nMethod 1 - Using double brackets [[]]:")
print(new_df_1.head(10))
print(f"Columns: {list(new_df_1.columns)}")
print(f"Shape: {new_df_1.shape}")

new_df_2 = df.loc[:, ["Patient_ID", "Ward", "Glucose_Reading", "Turnaround_Time"]]
print("\nMethod 2 - Using loc[:, [...]]:")
print(new_df_2.head(10))

print("\n" + "=" * 60)
print("HANDLING MISSING VALUES IN NEW DATAFRAME")
print("=" * 60)
print(f"\nMissing glucose values in new DataFrame: {new_df_1['Glucose_Reading'].isnull().sum()}")

glucose_avg = new_df_1["Glucose_Reading"].mean()
new_df_1["Glucose_Reading"] = new_df_1["Glucose_Reading"].fillna(glucose_avg)
print(f"After filling with mean ({glucose_avg:.2f}): {new_df_1['Glucose_Reading'].isnull().sum()} missing")

print("\n" + "=" * 60)
print("COMPLETE NEW DATAFRAME")
print("=" * 60)
print(new_df_1.to_string(index=False))

print("\n" + "=" * 60)
print("ANALYSIS ON NEW DATAFRAME")
print("=" * 60)
print(f"\nSummary Statistics:")
print(new_df_1.describe().to_string())

print(f"\nBy Ward:")
ward_summary = new_df_1.groupby("Ward").agg({
    "Patient_ID": "count",
    "Glucose_Reading": ["mean", "min", "max"],
    "Turnaround_Time": ["mean", "min", "max"]
}).round(2)
print(ward_summary)
