
import os
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

FOLDER = os.path.dirname(os.path.abspath(__file__))
EXCEL = os.path.join(FOLDER, "studenti.xlsx")
IZLAZ_XLSX = os.path.join(FOLDER, "rezultati.xlsx")
IZLAZ_CSV = os.path.join(FOLDER, "rezultati.csv")

# a) TODO: učitaj Grupa_A i Grupa_B
grupa_a = pd.read_excel(EXCEL, sheet_name="Grupa_A")
grupa_b = pd.read_excel(EXCEL, sheet_name="Grupa_B")

# b) TODO: kolona "grupa"
grupa_a["grupa"] = "A"
grupa_b["grupa"] = "B"
# c) TODO: concat
df = pd.concat([grupa_a, grupa_b], ignore_index=True)
print(df.shape)

# d) TODO: prosjek i polozio
df["prosjek"] = ((df["matematika"] + df["programiranje"] + df["statistika"]) / 3).round(2)

df["polozio"] = (
    (df["matematika"] >= 6) &
    (df["programiranje"] >= 6) &
    (df["statistika"] >= 6)
)

print(df.shape)
print("Polozilo:", df["polozio"].sum())
# e) TODO: ExcelWriter sa dva sheeta
with pd.ExcelWriter(IZLAZ_XLSX) as pisac:
    df.to_excel(pisac, sheet_name="Svi", index=False)

    df[df["polozio"]].to_excel(pisac, sheet_name="Polozili", index=False)

# f) TODO: Excel -> CSV i provjera
svi = pd.read_excel(IZLAZ_XLSX, sheet_name="Svi")
svi.to_csv(IZLAZ_CSV, index=False)

provjera = pd.read_csv(IZLAZ_CSV)
print(provjera.shape)

print("Zadatak 3 - dopuni TODO dijelove.")
