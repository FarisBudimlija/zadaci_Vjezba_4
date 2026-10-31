
import os
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

FOLDER = os.path.dirname(os.path.abspath(__file__))
FAJL = os.path.join(FOLDER, "studenti.csv")

# a) TODO: učitaj podatke i ispiši shape i head()
df = pd.read_csv(FAJL)

print("Dimenzije:", df.shape)
print(df.head())

# b) TODO: kolona prosjek
df["prosjek"] = (
    df["matematika"] +
    df["programiranje"] +
    df["statistika"]
) / 3

# c) TODO: top 5
top5 = df.sort_values(
    "prosjek",
    ascending=False,
    kind="stable"
).head(5)
print(top5[["ime", "smjer", "prosjek"]])
# d) TODO: value_counts
print(df["smjer"].value_counts())
# e) TODO: groupby
prosjek_smjer = df.groupby("smjer")["prosjek"].mean().sort_values(ascending=False)
print(prosjek_smjer)
# f) TODO: filtriranje prisustva
ispod_70 = df[df["prisustvo"] < 70]
print(ispod_70[["ime", "prisustvo"]])
# BONUS: TODO
df["polozio"] = (
    (df["matematika"] >= 6) &
    (df["programiranje"] >= 6) &
    (df["statistika"] >= 6)
)

print("Ukupno položilo:", df["polozio"].sum())

print("Položilo po smjeru:")
print(df.groupby("smjer")["polozio"].sum())

print("Zadatak 2 - dopuni TODO dijelove.")
