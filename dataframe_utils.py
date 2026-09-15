import pandas as pd

df = pd.read_csv('example.csv')
print(df.columns)
print(df.head())
print(df.describe())
print(df.info())
print(df.index)
print(df.ndim, df.shape, df.size)
