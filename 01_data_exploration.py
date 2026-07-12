import pandas as pd

df = pd.read_csv("dataset2.csv")
"""
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nMissing values:")
print(df.isna().sum())


print(
    df["Derived SEER Combined N (2016-2017)"]
    .value_counts(dropna=False)
)


print(df["Derived SEER Combined T (2016-2017)"].value_counts(dropna=False))

print(
    df["Derived AJCC T, 7th ed (2010-2015)"]
    .value_counts(dropna=False)
)
""" 

print(df["Derived SEER Combined T (2016-2017)"].value_counts(dropna=False))