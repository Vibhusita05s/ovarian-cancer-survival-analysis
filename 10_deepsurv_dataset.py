import pandas as pd

df = pd.read_csv("cox_ready.csv")

# age mapping
age_map = {
    "00 years":0,
    "01-04 years":2.5,
    "05-09 years":7,
    "10-14 years":12,
    "15-19 years":17,
    "20-24 years":22,
    "25-29 years":27,
    "30-34 years":32,
    "35-39 years":37,
    "40-44 years":42,
    "45-49 years":47,
    "50-54 years":52,
    "55-59 years":57,
    "60-64 years":62,
    "65-69 years":67,
    "70-74 years":72,
    "75-79 years":77,
    "80-84 years":82,
    "85-89 years":87,
    "90+ years":92
}

df["age_num"] = df["Age recode with <1 year olds and 90+"].map(age_map)

# histology grouping
histology_map = {
    8380:"Endometrioid",
    8381:"Endometrioid",
    8382:"Endometrioid",
    8441:"Serous",
    8460:"Serous",
    8461:"Serous",
    8462:"Serous",
    8463:"Serous",
    8470:"Mucinous",
    8471:"Mucinous",
    8472:"Mucinous",
    8480:"Mucinous",
    8481:"Mucinous",
    8482:"Mucinous",
    8560:"Other",
    8570:"Other",
    9014:"Other",
    9015:"Other"
}

df["Histology_Group"] = (
    df["Histologic Type ICD-O-3"]
    .map(histology_map)
)

model_df = df[
    [
        "Survival months",
        "event",
        "age_num",
        "Marital status at diagnosis",
        "Grade Recode (thru 2017)",
        "Histology_Group",
        "T_stage",
        "N_stage",
        "SEER Combined Mets at DX-bone (2010+)",
        "SEER Combined Mets at DX-liver (2010+)",
        "SEER Combined Mets at DX-lung (2010+)"
    ]
]

model_df = pd.get_dummies(
    model_df,
    drop_first=True
)

model_df = model_df.rename(
    columns={
        "Survival months":"time"
    }
)

model_df.to_csv(
    "deepsurv_dataset.csv",
    index=False
)

print(model_df.shape)
print("saved as deepsurv_dataset.csv")