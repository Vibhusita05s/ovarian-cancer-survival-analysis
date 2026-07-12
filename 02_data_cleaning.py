import pandas as pd

# Load dataset
df = pd.read_csv("dataset2.csv")

# -----------------------------
# Create unified T stage
# -----------------------------
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

# -----------------------------
# Simplify T stage
# -----------------------------
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

# -----------------------------
# Check T stage counts
# -----------------------------
print("\n===== T_stage =====")
print(df["T_stage"].value_counts(dropna=False))

# -----------------------------
# Save value counts of ALL columns
# -----------------------------
with open("value_counts.txt", "w", encoding="utf-8") as f:

    for col in df.columns:

        f.write("\n")
        f.write("=" * 60)
        f.write("\n")

        f.write(f"{col}\n")

        f.write("=" * 60)
        f.write("\n")

        f.write(str(df[col].value_counts(dropna=False)))

        f.write("\n\n")

print("\nvalue_counts.txt created successfully!")