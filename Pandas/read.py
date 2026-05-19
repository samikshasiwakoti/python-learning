import pandas as pd

df = pd.read_csv("titanic.csv")
print(df)
print(df.head())
print(df.tail())
print(df.sample(5))
print(df.info())
print(df.describe())
print(df.columns)
print(df["Name"])
print(df.iloc[0])# first row by postioning
print(df.iloc[0:2])# first 2 row
print(df.iloc[:, 0])# everything
print(df[df['Age']<30])
print(df[(df["Sex"] == "Female") & (df["Survived"] ==1)])




