"""Practice Task 1: Find and remove duplicate rows"""

import pandas as pd

sample_data = """Product,Price,Stock
Laptop,1000,50
Mouse,25,200
Keyboard,75,150
Laptop,1000,50
Monitor,300,75
Mouse,25,200
Headphones,100,120
Laptop,1000,50
Tablet,200,60"""

with open("sample_products.csv", "w") as f:
    f.write(sample_data)

print("=" * 70)
print("PRACTICE TASK 1: FIND AND REMOVE DUPLICATE ROWS")
print("=" * 70)

df = pd.read_csv("sample_products.csv")

print("\n[Step 1] Original DataFrame:")
print(df.to_string(index=False))
print(f"\nTotal rows: {len(df)}")

duplicates = df.duplicated()
num_duplicates = duplicates.sum()

print(f"\n[Step 2] Duplicate Detection:")
print(f"  Number of duplicate rows: {num_duplicates}")
print(f"  Duplicate mask: {list(duplicates)}")

print(f"\n[Step 3] Duplicate rows:")
duplicate_rows = df[duplicates]
print(duplicate_rows.to_string(index=False))

df_cleaned = df.drop_duplicates()

print(f"\n[Step 4] After removing duplicates:")
print(df_cleaned.to_string(index=False))
print(f"\nRows before: {len(df)}, After: {len(df_cleaned)}")
print(f"Duplicates removed: {len(df) - len(df_cleaned)}")

print("\n" + "=" * 60)
print("ALTERNATIVE: keep='last' option")
print("=" * 60)
df_keep_last = df.drop_duplicates(keep="last")
print(df_keep_last.to_string(index=False))

print("\n" + "=" * 60)
print("ALTERNATIVE: Subset of columns for duplicate detection")
print("=" * 60)
df_subset = df.drop_duplicates(subset=["Product", "Price"])
print(df_subset.to_string(index=False))
print("Note: Only checks duplicates based on Product and Price columns")
