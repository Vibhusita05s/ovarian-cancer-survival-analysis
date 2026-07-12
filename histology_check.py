
import pandas as pd

df = pd.read_csv("dataset2.csv")

histology_map = {
    8380: "Endometrioid adenocarcinoma",
    8381: "Endometrioid adenofibroma, malignant",
    8382: "Endometrioid adenocarcinoma, secretory variant",

    8441: "Serous cystadenocarcinoma",

    8460: "Papillary serous cystadenocarcinoma",
    8461: "Serous surface papillary carcinoma",
    8462: "Serous adenocarcinoma",
    8463: "Serous carcinoma",

    8470: "Mucinous cystadenocarcinoma",
    8471: "Papillary mucinous cystadenocarcinoma",
    8472: "Mucinous adenocarcinoma",

    8480: "Mucinous adenocarcinoma",
    8481: "Mucin-producing adenocarcinoma",
    8482: "Mucinous carcinoma",

    8560: "Adenosquamous carcinoma",
    8570: "Adenocarcinoma with squamous metaplasia",

    9014: "Mesonephroma, malignant",
    9015: "Mesonephric adenocarcinoma"
}

for code in sorted(df["Histologic Type ICD-O-3"].unique()):
    print(code, "->", histology_map.get(code, "Unknown"))
    print(df["RX Summ--Surg Prim Site (1998-2022)"].value_counts())
    print(sorted(df["RX Summ--Surg Prim Site (1998-2022)"].unique()))