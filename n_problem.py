import pandas as pd

df = pd.read_csv("dataset2.csv")

ajcc_blank = (
    df["Derived AJCC N, 7th ed (2010-2015)"] == "Blank(s)"
).sum()

seer_blank = (
    df["Derived SEER Combined N (2016-2017)"] == "Blank(s)"
).sum()

print("AJCC blanks:", ajcc_blank)
print("SEER blanks:", seer_blank)
print(
    df["Derived SEER Combined N (2016-2017)"]
    .value_counts(dropna=False)
)