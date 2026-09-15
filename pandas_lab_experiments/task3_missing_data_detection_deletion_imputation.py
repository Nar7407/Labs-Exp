
import pandas as pd
import numpy as np

data = {
    "Sensor_ID": ["S001", "S002", "S003", "S004", "S005",
                  "S006", "S007", "S008", "S009", "S010",
                  "S011", "S012"],
    "Temperature": [25.5, np.nan, 28.3, 26.1, np.nan,
                    27.8, 25.0, np.nan, 29.2, 26.7,
                    27.5, np.nan],
    "Humidity": [65.2, 70.1, np.nan, 68.5, 72.3,
                 np.nan, 66.8, 71.0, np.nan, 69.5,
                 67.2, np.nan],
    "Status": ["Normal", "Normal", "Alert", np.nan, "Normal",
               "Normal", np.nan, "Alert", "Normal", np.nan,
               "Normal", "Normal"]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print()

missing_count = df.isnull().sum()
missing_percentage = (missing_count / len(df)) * 100

print("Missing Values Analysis:")
print(f"{'Column':<15} {'Missing Count':<15} {'Missing %'}")
print("-" * 45)
for col in df.columns:
    print(f"{col:<15} {missing_count[col]:<15} {missing_percentage[col]:.2f}%")
print()

df_dropped = df.dropna()
print(f"Strategy 1 - dropna():")
print(f"  Rows retained: {len(df_dropped)} out of {len(df)} ({len(df_dropped)/len(df)*100:.2f}%)")
print(df_dropped)
print()

df_filled = df.copy()
df_filled["Temperature"] = df_filled["Temperature"].fillna(df_filled["Temperature"].mean())
df_filled["Humidity"] = df_filled["Humidity"].fillna(df_filled["Humidity"].mean())
status_mode = df_filled["Status"].mode()[0]
df_filled["Status"] = df_filled["Status"].fillna(status_mode)

print(f"Strategy 2 - fillna():")
print(f"  Rows retained: {len(df_filled)} out of {len(df)} ({len(df_filled)/len(df)*100:.2f}%)")
print(df_filled)
print()

print("=" * 60)
print("COMPARISON OF STRATEGIES")
print("=" * 60)
print(f"dropna()    : {len(df_dropped)} rows retained ({len(df_dropped)/len(df)*100:.2f}%)")
print(f"fillna()    : {len(df_filled)} rows retained ({len(df_filled)/len(df)*100:.2f}%)")

justification = """
JUSTIFICATION:

For this sensor log dataset, fillna() with mean/mode imputation is more appropriate because:

1. DATA RETENTION: The dataset has only 12 records. dropna() would remove 7 out of 12 rows
   (58.33% data loss), which is significant for small datasets. Losing more than half the data
   could lead to loss of valuable information and biased analysis.

2. SENSOR CONTINUITY: In sensor monitoring applications, each sensor reading is important for
   detecting trends over time. Removing entire rows means losing all other sensor readings
   for that timestamp, even if some values were valid.

3. MISSINGNESS PATTERN: The missing values appear to be random sensor failures rather than
   systematic issues. Mean imputation for temperature/humidity and mode for status is reasonable
   when missingness is random and won't significantly bias the overall statistics.

4. WHEN dropna() WOULD BE PREFERRED:
   - When missing values exceed 50% in a column
   - When missingness is not random (MNAR - Missing Not At Random)
   - When accurate values are critical (e.g., patient diagnosis)
   - When we have abundant data and losing some rows won't impact analysis

5. WHEN fillna() IS PREFERRED:
   - Small datasets where every row matters
   - When we need to preserve all records for downstream analysis
   - When missingness is random (MCAR - Missing Completely At Random)
   - When we can reasonably estimate missing values from existing data
"""
print(justification)
