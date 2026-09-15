import pandas as pd

# Load the sample CSV and inspect basic DataFrame attributes
df = pd.read_csv('example.csv')
print(df.columns)      # column labels
print(df.head())       # first five rows
print(df.describe())   # numeric summary statistics
print(df.info())       # dtypes and non-null counts
print(df.index)        # row index labels
print(df.ndim, df.shape, df.size)  # dimensions, shape and total element count
