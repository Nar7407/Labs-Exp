"""Practice Task 4: Compute correlation matrix and find most correlated columns"""

import pandas as pd
import numpy as np

print("=" * 70)
print("PRACTICE TASK 4: CORRELATION MATRIX ANALYSIS")
print("=" * 70)

np.random.seed(42)
n_samples = 50

data = {
    "Study_Hours": np.random.uniform(1, 10, n_samples),
    "Attendance": np.random.uniform(60, 100, n_samples),
    "Assignment_Score": np.random.uniform(50, 100, n_samples),
    "Midterm_Score": np.random.uniform(55, 100, n_samples),
    "Final_Score": np.random.uniform(50, 100, n_samples),
    "Sleep_Hours": np.random.uniform(4, 9, n_samples)
}

df = pd.DataFrame(data)

df["Final_Score"] = (
    df["Study_Hours"] * 5 + 
    df["Midterm_Score"] * 0.5 + 
    df["Assignment_Score"] * 0.3 +
    np.random.normal(0, 5, n_samples)
)

df["Midterm_Score"] = (
    df["Attendance"] * 0.3 +
    df["Assignment_Score"] * 0.4 +
    np.random.normal(0, 5, n_samples)
)

print("\n[Step 1] Sample Data:")
print(df.head(10).to_string(index=False))

print("\n" + "=" * 70)
print("[Step 2] Correlation Matrix:")
print("=" * 70)

corr_matrix = df.corr()
print(corr_matrix.round(3).to_string())

print("\n" + "=" * 70)
print("[Step 3] MOST STRONGLY CORRELATED PAIRS")
print("=" * 70)

upper_triangle = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))

max_corr = upper_triangle.max().max()
max_corr_location = np.where(upper_triangle == max_corr)
col1 = upper_triangle.columns[max_corr_location[1][0]]
col2 = upper_triangle.index[max_corr_location[0][0]]

print(f"\nSTRONGEST CORRELATION: {col1} vs {col2}")
print(f"    Correlation Coefficient: {max_corr:.4f}")

upper_triangle_copy = upper_triangle.copy()
upper_triangle_copy.iloc[max_corr_location[0][0], max_corr_location[1][0]] = np.nan
second_max_corr = upper_triangle_copy.max().max()
second_max_location = np.where(upper_triangle_copy == second_max_corr)
col3 = upper_triangle_copy.columns[second_max_location[1][0]]
col4 = upper_triangle_copy.index[second_max_location[0][0]]

print(f"\nSECOND STRONGEST: {col3} vs {col4}")
print(f"    Correlation Coefficient: {second_max_corr:.4f}")

print("\n" + "=" * 70)
print("[Step 4] TOP 5 MOST CORRELATED PAIRS")
print("=" * 70)

corr_pairs = []
for i in range(len(corr_matrix.columns)):
    for j in range(i + 1, len(corr_matrix.columns)):
        corr_pairs.append({
            "Variable_1": corr_matrix.columns[i],
            "Variable_2": corr_matrix.columns[j],
            "Correlation": corr_matrix.iloc[i, j]
        })

corr_df = pd.DataFrame(corr_pairs)
corr_df_sorted = corr_df.sort_values("Correlation", ascending=False)

print("\nTop 5 Correlations:")
print("-" * 55)
print(f"{'Rank':<6}{'Variable 1':<20}{'Variable 2':<20}{'Correlation':<12}")
print("-" * 55)
for rank, (_, row) in enumerate(corr_df_sorted.head(5).iterrows(), 1):
    print(f"{rank:<6}{row['Variable_1']:<20}{row['Variable_2']:<20}{row['Correlation']:<12.4f}")
print("-" * 55)

print("\n" + "=" * 70)
print("[Step 5] INTERPRETATION")
print("=" * 70)

print(f"""
Correlation Coefficient Interpretation:
  - +1.0: Perfect positive correlation
  - +0.7 to +0.9: Strong positive correlation
  - +0.3 to +0.7: Moderate positive correlation
  - 0 to +0.3: Weak positive correlation
  - 0: No correlation
  - -0.3 to 0: Weak negative correlation
  - -0.7 to -0.3: Moderate negative correlation
  - -0.9 to -0.7: Strong negative correlation
  - -1.0: Perfect negative correlation

Strongest correlation in this dataset:
  {col1} and {col2} have a correlation of {max_corr:.4f}
  This means as {col1.lower()} increases, {col2.lower()} tends to 
  {'increase' if max_corr > 0 else 'decrease'} as well.
""")

print("\nFull Correlation Matrix (heatmap-style):")
print(corr_matrix.round(2).to_string())
