import pandas as pd
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(
    "final_model_comparison.csv"
)

models = df["Model"]

# =====================
# C-INDEX
# =====================

plt.figure(figsize=(8,5))

plt.bar(
    models,
    df["C-index"]
)

plt.ylabel("C-index")
plt.title("Model Comparison: C-index")

plt.savefig(
    "cindex_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# =====================
# AUC COMPARISON
# =====================

x = np.arange(len(models))
width = 0.35

plt.figure(figsize=(8,5))

plt.bar(
    x - width/2,
    df["3-Year AUC"],
    width,
    label="3-Year AUC"
)

plt.bar(
    x + width/2,
    df["5-Year AUC"],
    width,
    label="5-Year AUC"
)

plt.xticks(x, models)

plt.ylabel("AUC")

plt.title(
    "3-Year and 5-Year AUC Comparison"
)

plt.legend()

plt.savefig(
    "auc_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Saved:")
print("cindex_comparison.png")
print("auc_comparison.png")