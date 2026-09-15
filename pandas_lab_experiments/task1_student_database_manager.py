"""Pandas Laboratory - Task 1: Student Database Manager"""

import pandas as pd
import numpy as np

data = {
    "Name": ["Aditi", "Rohan", "Priya", "Kabir", "Sneha", "Amit", "Neha", "Vikram"],
    "Branch": ["CS", "EC", "CS", "ME", "CS", "EC", "ME", "CS"],
    "Age": [20, 21, 20, 22, 19, 21, 20, 22],
    "CGPA": [8.2, 7.0, 9.1, 6.8, 7.8, 8.5, 7.2, 8.9]
}

df = pd.DataFrame(data)
print("Initial DataFrame:")
print(df)
print()

df["Status"] = np.where(df["CGPA"] >= 7.5, "Eligible", "Not Eligible")
print("DataFrame after adding Status column:")
print(df)
print()

new_row1 = {"Name": "Rahul", "Branch": "IT", "Age": 20, "CGPA": 8.0, "Status": "Eligible"}
new_row2 = {"Name": "Pooja", "Branch": "CS", "Age": 21, "CGPA": 7.9, "Status": "Eligible"}
df.loc[len(df)] = new_row1
df.loc[len(df)] = new_row2
print("DataFrame after adding 2 new rows:")
print(df)
print()

df = df.drop(1, axis=0)
print("DataFrame after deleting row at index 1:")
print(df)
print()

df_sorted = df.sort_values(by="CGPA", ascending=False)
print("DataFrame sorted by CGPA (descending):")
print(df_sorted)
print()

print("Summary Statistics (describe):")
print(df.describe())
