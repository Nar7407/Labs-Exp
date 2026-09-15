import pandas as pd

# Load the dataset and inspect basic DataFrame attributes
df = pd.read_csv("student.csv",)
print(df.columns)   # column labels
print(df.head())    # first five rows
print(df.describe())  # summary statistics of numeric columns

print(df.index)     # row index labels

# Sorting, scalar lookups and group-by aggregation
print(df.sort_values('CarName', ascending=False))  # sort by CarName, descending
print(df.sort_index())                             # restore original index order
print(df.at[0, 'CarName'])                         # label-based scalar lookup
print(df.iat[0, 0])                                # position-based scalar lookup
print(df.groupby('CarName')['carlength'].mean())   # mean carlength per CarName