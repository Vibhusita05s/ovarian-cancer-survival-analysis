import pandas as pd

df = pd.read_csv("final_cohort.csv")

print("Shape:")
print(df.shape)

# =====================================================
# CREATE EVENT COLUMN
# =====================================================

df["event"] = df["Vital status recode (study cutoff used)"].map({
    "Dead": 1,
    "Alive": 0
})

print("\nEvent Counts:")
print(df["event"].value_counts())

print("\nMissing Event Values:")
print(df["event"].isna().sum())

# Save for next step
df.to_csv("cox_ready.csv", index=False)

print("\ncox_ready.csv saved successfully!")