import pandas as pd

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv("dataset2.csv")

# =====================================================
# CREATE T STAGE
# =====================================================

def combine_t_stage(row):
    ajcc = str(row["Derived AJCC T, 7th ed (2010-2015)"])
    seer = str(row["Derived SEER Combined T (2016-2017)"])

    if ajcc != "Blank(s)":
        return ajcc
    elif seer != "Blank(s)":
        return seer
    else:
        return "Unknown"

df["T_stage_raw"] = df.apply(combine_t_stage, axis=1)


def simplify_t_stage(stage):
    stage = str(stage)

    if stage.startswith(("T3", "p3", "c3")):
        return "T3"

    elif stage.startswith(("T1", "T2", "p1", "p2", "c1", "c2")):
        return "T1-T2"

    elif stage == "T0":
        return "T1-T2"

    else:
        return "Unknown"

df["T_stage"] = df["T_stage_raw"].apply(simplify_t_stage)

# =====================================================
# CREATE N STAGE
# =====================================================

def combine_n_stage(row):
    ajcc = str(row["Derived AJCC N, 7th ed (2010-2015)"])
    seer = str(row["Derived SEER Combined N (2016-2017)"])

    if ajcc != "Blank(s)":
        return ajcc
    elif seer != "Blank(s)":
        return seer
    else:
        return "Unknown"

df["N_stage_raw"] = df.apply(combine_n_stage, axis=1)


def simplify_n_stage(stage):
    stage = str(stage)

    if stage in ["N0", "p0", "c0"]:
        return "N0"

    elif stage in ["N1", "p1", "c1"]:
        return "N1"

    else:
        return "Unknown"

df["N_stage"] = df["N_stage_raw"].apply(simplify_n_stage)

# =====================================================
# FINAL COHORT FILTERS
# =====================================================

final_cohort = df[
    (df["RX Summ--Surg Prim Site (1998-2022)"] != 0) &
    (df["Grade Recode (thru 2017)"] != "Unknown") &
    (df["Marital status at diagnosis"] != "Unknown") &
    (df["Survival months"] != "Unknown") &
    (df["T_stage"] != "Unknown") &
    (df["N_stage"] != "Unknown") &
    (df["Chemotherapy recode (yes, no/unk)"] == "Yes") &
    (df["SEER Combined Mets at DX-bone (2010+)"] != "Unknown") &
    (df["SEER Combined Mets at DX-brain (2010+)"] != "Unknown") &
    (df["SEER Combined Mets at DX-liver (2010+)"] != "Unknown") &
    (df["SEER Combined Mets at DX-lung (2010+)"] != "Unknown")
]

print("Original cohort:", len(df))
print("Final cohort:", len(final_cohort))

final_cohort.to_csv("final_cohort.csv", index=False)

print("\nfinal_cohort.csv saved successfully!")