"""Practice Task 2: Rename columns and reset index after filtering"""

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"],
    "Score": [85, 92, 78, 95, 68, 88, 72],
    "Subject": ["Math", "Math", "Science", "Science", "Math", "Science", "Math"]
}

df = pd.DataFrame(data)

print("=" * 70)
print("PRACTICE TASK 2: RENAME COLUMNS AND RESET INDEX")
print("=" * 70)

print("\n[Step 1] Original DataFrame:")
print(df.to_string(index=False))
print(f"\nIndex: {list(df.index)}")

df_filtered = df[df["Score"] >= 80]
print(f"\n[Step 2] After filtering (Score >= 80):")
print(df_filtered.to_string(index=False))
print(f"\nIndex after filtering: {list(df_filtered.index)}")

df_reset = df_filtered.reset_index(drop=True)
print(f"\n[Step 3] After reset_index(drop=True):")
print(df_reset.to_string(index=False))
print(f"\nIndex after reset: {list(df_reset.index)}")

df_renamed = df_reset.rename(columns={
    "Name": "Student_Name",
    "Score": "Exam_Score",
    "Subject": "Course"
})
print(f"\n[Step 4] After renaming columns:")
print(df_renamed.to_string(index=False))
print(f"\nNew columns: {list(df_renamed.columns)}")

print("\n" + "=" * 70)
print("ALTERNATIVE METHODS")
print("=" * 70)

df_method1 = df[df["Score"] >= 80].reset_index(drop=True)
df_method1.rename(columns={
    "Name": "Student",
    "Score": "Marks",
    "Subject": "Topic"
}, inplace=True)
print("\nMethod 1 - Using inplace=True:")
print(df_method1.to_string(index=False))

df_method2 = df[df["Score"] >= 80].reset_index(drop=True)
df_method2.columns = ["Student", "Marks", "Topic"]
print("\nMethod 2 - Direct column assignment:")
print(df_method2.to_string(index=False))

df_chained = (df[df["Score"] >= 80]
              .reset_index(drop=True)
              .rename(columns={"Name": "Student", "Score": "Marks", "Subject": "Topic"}))
print("\nMethod 3 - Chained operations:")
print(df_chained.to_string(index=False))
