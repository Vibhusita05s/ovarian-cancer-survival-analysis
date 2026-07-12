# 12_prepare_tensors.py

import pandas as pd
import numpy as np

# =========================
# LOAD TRAIN DATA
# =========================

df = pd.read_csv("train.csv")

print("Original shape:", df.shape)

# =========================
# CONVERT BOOL -> INT
# =========================

bool_cols = df.select_dtypes(include="bool").columns

df[bool_cols] = df[bool_cols].astype(int)

# =========================
# SPLIT FEATURES / TARGETS
# =========================

X = df.drop(
    columns=["time", "event"]
)

time = df["time"]

event = df["event"]

# =========================
# CHECK
# =========================

print("\nFeature shape:", X.shape)
print("Time shape:", time.shape)
print("Event shape:", event.shape)

print("\nFeature dtypes:")
print(X.dtypes)

# =========================
# SAVE CLEAN VERSION
# =========================

clean_df = pd.concat(
    [time, event, X],
    axis=1
)

clean_df.to_csv(
    "train_clean.csv",
    index=False
)

print("\nSaved train_clean.csv")