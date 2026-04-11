import pandas as pd

df = pd.read_csv('./Sales Dataset.csv')
df["Order Date"] = pd.to_datetime(df["Order Date"])
print("min date: ")
print(df["Order Date"].min())
print("max date: ")
print(df["Order Date"].max())
print("Category counts: ")
print(df["Category"].value_counts())
print("row amount")
print(df.count())