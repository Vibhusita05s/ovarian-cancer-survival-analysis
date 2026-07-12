import pandas as pd
from lifelines import CoxPHFitter

df = pd.read_csv("cox_ready.csv")

# convert age groups to midpoint
age_map = {
    "00 years": 0,
    "01-04 years": 2.5,
    "05-09 years": 7,
    "10-14 years": 12,
    "15-19 years": 17,
    "20-24 years": 22,
    "25-29 years": 27,
    "30-34 years": 32,
    "35-39 years": 37,
    "40-44 years": 42,
    "45-49 years": 47,
    "50-54 years": 52,
    "55-59 years": 57,
    "60-64 years": 62,
    "65-69 years": 67,
    "70-74 years": 72,
    "75-79 years": 77,
    "80-84 years": 82,
    "85-89 years": 87,
    "90+ years": 92,
}

df["age_num"] = df["Age recode with <1 year olds and 90+"].map(age_map)

cox_df = df[["Survival months", "event", "age_num"]]

cox_df.columns = ["time", "event", "age"]

cph = CoxPHFitter()
cph.fit(cox_df, duration_col="time", event_col="event")

cph.print_summary()

