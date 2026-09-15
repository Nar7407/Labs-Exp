"""AI Case Study: Patient Test-Result Analysis using Pandas DataFrame - Task 4"""

import os
import pandas as pd

df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "patient_tests.csv"))

print("=" * 60)
print("HANDLING MISSING GLUCOSE VALUES")
print("=" * 60)

print("\nMissing values BEFORE handling:")
print(df.isnull().sum())

glucose_avg = df["Glucose_Reading"].mean()
print(f"\nAverage glucose reading (from available data): {glucose_avg:.2f} mg/dL")

df["Glucose_Reading"] = df["Glucose_Reading"].fillna(glucose_avg)

print("\nMissing values AFTER handling:")
print(df.isnull().sum())

remaining_missing = df["Glucose_Reading"].isnull().sum()
print(f"\nVerification:")
print(f"  Remaining missing glucose values: {remaining_missing}")
if remaining_missing == 0:
    print("  SUCCESS: No missing glucose values remain!")
else:
    print("  WARNING: Missing values still present!")

print("\nUpdated Glucose_Reading values:")
print(df[["Patient_ID", "Glucose_Reading"]].to_string(index=False))
