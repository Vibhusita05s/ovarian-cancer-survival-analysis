import pandas as pd

# Load multivariate results
df = pd.read_csv("multivariate_cox_results.csv")

# Keep only significant variables
significant = df[df["p"] < 0.05]

# Sort by p-value
significant = significant.sort_values("p")

# Save
significant.to_csv(
    "significant_variables.csv",
    index=False
)

print("\nSignificant Variables (p < 0.05)\n")
print(
    significant[
        [
            "coef",
            "exp(coef)",
            "p"
        ]
    ]
)

print("\nSaved as significant_variables.csv")


feature_names = significant["covariate"].tolist()

print("\nSelected Features:\n")

for f in feature_names:
    print(f)
    
