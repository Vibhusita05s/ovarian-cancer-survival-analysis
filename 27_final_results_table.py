import pandas as pd

results = pd.DataFrame({
    "Model": [
        "CoxPH",
        "DeepSurv",
        "RSF",
        "DeepHit"
    ],
    "C-index": [
        0.6794,
        0.6815,
        0.6790,
        0.6860
    ],
    "3-Year AUC": [
        0.7128,
        0.7184,
        0.7117,
        0.6885
    ],
    "5-Year AUC": [
        0.7293,
        0.7307,
        0.7287,
        0.7124
    ]
})

print(results)

results.to_csv(
    "final_model_comparison.csv",
    index=False
)

print("\nSaved: final_model_comparison.csv")