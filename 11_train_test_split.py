# 11_train_test_split.py

import pandas as pd
from sklearn.model_selection import train_test_split

# =========================
# LOAD DATA
# =========================

df = pd.read_csv("deepsurv_dataset.csv")

print("Full dataset shape:", df.shape)

# =========================
# TRAIN / TEMP
# =========================

train_df, temp_df = train_test_split(
    df,
    test_size=0.30,
    random_state=42
)

# =========================
# VALID / TEST
# =========================

valid_df, test_df = train_test_split(
    temp_df,
    test_size=0.50,
    random_state=42
)

# =========================
# SAVE FILES
# =========================

train_df.to_csv(
    "train.csv",
    index=False
)

valid_df.to_csv(
    "valid.csv",
    index=False
)

test_df.to_csv(
    "test.csv",
    index=False
)

# =========================
# CHECK SHAPES
# =========================

print("\nTrain shape:", train_df.shape)
print("Validation shape:", valid_df.shape)
print("Test shape:", test_df.shape)

print("\nFiles saved:")
print("train.csv")
print("valid.csv")
print("test.csv")