import pandas as pd

df = pd.read_csv("student.csv",)
print(df.columns)
print(df.head())
print(df.describe())

print(df.index)

print(df.sort_values('CarName', ascending=False))
print(df.sort_index())
print(df.at[0, 'CarName'])
print(df.iat[0, 0])
print(df.groupby('CarName')['carlength'].mean())