"""Practice Task 3: Merge two DataFrames using pd.merge()"""

import pandas as pd

print("=" * 70)
print("PRACTICE TASK 3: MERGE TWO DATAFRAMES")
print("=" * 70)

students = pd.DataFrame({
    "Student_ID": ["S001", "S002", "S003", "S004", "S005"],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Class": ["10A", "10B", "10A", "10C", "10B"]
})

marks = pd.DataFrame({
    "Student_ID": ["S001", "S002", "S003", "S004", "S006"],
    "Math": [85, 92, 78, 95, 88],
    "Science": [72, 88, 90, 85, 91],
    "English": [80, 75, 82, 90, 78]
})

print("\n[Step 1] Students DataFrame:")
print(students.to_string(index=False))

print("\n[Step 2] Marks DataFrame:")
print(marks.to_string(index=False))

print("\n" + "=" * 70)
print("MERGE OPERATIONS")
print("=" * 70)

print("\n[3a] INNER JOIN (default):")
inner_merged = pd.merge(students, marks, on="Student_ID", how="inner")
print(inner_merged.to_string(index=False))
print(f"Rows: {len(inner_merged)} (only common Student_IDs)")

print("\n[3b] LEFT JOIN (all students):")
left_merged = pd.merge(students, marks, on="Student_ID", how="left")
print(left_merged.to_string(index=False))
print(f"Rows: {len(left_merged)} (all students, NaN for missing marks)")

print("\n[3c] RIGHT JOIN (all marks):")
right_merged = pd.merge(students, marks, on="Student_ID", how="right")
print(right_merged.to_string(index=False))
print(f"Rows: {len(right_merged)} (all marks, NaN for missing student info)")

print("\n[3d] OUTER JOIN (all records):")
outer_merged = pd.merge(students, marks, on="Student_ID", how="outer")
print(outer_merged.to_string(index=False))
print(f"Rows: {len(outer_merged)} (all records from both DataFrames)")

print("\n" + "=" * 70)
print("MERGE WITH DIFFERENT COLUMN NAMES")
print("=" * 70)

students2 = pd.DataFrame({
    "ID": ["S001", "S002", "S003"],
    "Name": ["Alice", "Bob", "Charlie"]
})

marks2 = pd.DataFrame({
    "Student_ID": ["S001", "S002", "S003"],
    "Math": [85, 92, 78]
})

print("\nStudents2 (key column: 'ID'):")
print(students2.to_string(index=False))
print("\nMarks2 (key column: 'Student_ID'):")
print(marks2.to_string(index=False))

print("\nMerged using left_on and right_on:")
merged_diff_keys = pd.merge(students2, marks2, left_on="ID", right_on="Student_ID")
print(merged_diff_keys.to_string(index=False))

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

summary = """
Merge Types:
- inner: Only rows with matching keys in both DataFrames (default)
- left: All rows from left DataFrame, matching from right
- right: All rows from right DataFrame, matching from left
- outer: All rows from both DataFrames, NaN where no match

Use Cases:
- Inner: When you only need complete records
- Left: When left table is primary and right is supplementary
- Right: When right table is primary
- Outer: When you need to see all data including mismatches
"""
print(summary)
