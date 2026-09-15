"""Additional Question 10: Export processed DataFrame to CSV"""

import pandas as pd
import os

df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ai_case_study", "patient_tests.csv"))

print("=" * 70)
print("Q10: EXPORT PROCESSED DATAFRAME TO CSV")
print("=" * 70)

print("\n[Step 1] Load original data")
print(f"  Shape: {df.shape}")
print(f"  Missing values: {df.isnull().sum().sum()}")

glucose_mean = df["Glucose_Reading"].mean()
df["Glucose_Reading"] = df["Glucose_Reading"].fillna(glucose_mean)
print(f"\n[Step 2] Handle missing glucose values")
print(f"  Mean used for imputation: {glucose_mean:.2f} mg/dL")
print(f"  Remaining missing glucose: {df['Glucose_Reading'].isnull().sum()}")

df["Status"] = df["Glucose_Reading"].apply(lambda x: "High" if x > 140 else "Normal")
print(f"\n[Step 3] Add computed columns")
print(f"  Added 'Status' column (High/Normal based on 140 mg/dL threshold)")

df_sorted = df.sort_values(by="Turnaround_Time", ascending=False)
print(f"\n[Step 4] Sort by turnaround time (descending)")

df_sorted = df_sorted.reset_index(drop=True)
print(f"\n[Step 5] Reset index")

output_file = "processed_patient_tests.csv"
df_sorted.to_csv(output_file, index=False)
print(f"\n[Step 6] Export to CSV")
print(f"  File: {output_file}")
print(f"  Rows: {len(df_sorted)}")
print(f"  Columns: {list(df_sorted.columns)}")

print(f"\n[Step 7] Verify exported file")
df_verified = pd.read_csv(output_file)
print(f"  Successfully loaded back: {len(df_verified)} rows")
print(f"  Columns match: {list(df_verified.columns) == list(df_sorted.columns)}")

print("\n" + "=" * 70)
print("EXPORTED DATA PREVIEW")
print("=" * 70)
print(df_sorted.to_string(index=False))

print("\n" + "=" * 70)
print(f"SUCCESS: Data exported to '{output_file}'")
print("=" * 70)

if os.path.exists(output_file):
    file_size = os.path.getsize(output_file)
    print(f"\nFile size: {file_size} bytes")
