import os
import pandas as pd

df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ai_case_study", "patient_tests.csv"))

print("=" * 70)
print("Q3: REMOVE ROWS WITH MISSING ANALYTE VALUES (dropna)")
print("=" * 70)

print("\nOriginal DataFrame:")
print(f"  Total rows: {len(df)}")
print(f"  Missing values per column:")
for col in df.columns:
    missing = df[col].isnull().sum()
    if missing > 0:
        print(f"    - {col}: {missing} missing")

df_cleaned = df.dropna()

print(f"\nAfter dropna():")
print(f"  Remaining rows: {len(df_cleaned)}")
print(f"  Rows removed: {len(df) - len(df_cleaned)}")
print(f"  Percentage retained: {(len(df_cleaned)/len(df))*100:.2f}%")

print(f"\nRemaining rows:")
print(df_cleaned.to_string(index=False))

print("\n" + "=" * 70)
print("DISCUSSION")
print("=" * 70)

discussion = f"""
Effect of removing rows with missing values:

1. DATA LOSS:
   - {len(df) - len(df_cleaned)} out of {len(df)} rows removed ({((len(df) - len(df_cleaned))/len(df))*100:.1f}% loss)
   - This is significant for small datasets

2. WHEN TO USE dropna():
   - Missing data is minimal (<5% of rows)
   - Missingness is NOT random (MNAR - systematic issue)
   - More data is available from other sources
   - Analysis requires complete cases only

3. IMPACT ON ANALYSIS:
   - Statistics calculated on remaining data only
   - May introduce bias if missing pattern is not random
   - Ward representation may become unbalanced

4. ALTERNATIVE:
   - For this dataset, imputation (fillna) preserves more information
   - dropna() is better when data quality is critical and missingness
     indicates unreliable measurements
"""
print(discussion)
