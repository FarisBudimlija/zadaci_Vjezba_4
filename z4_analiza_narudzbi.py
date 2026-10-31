
import os
import pandas as pd
from matplotlib import pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

FOLDER = os.path.dirname(os.path.abspath(__file__))
FAJL = os.path.join(FOLDER, "narudzbe.csv")
DANI = ["Pon", "Uto", "Sri", "Čet", "Pet", "Sub", "Ned"]   # 0 = ponedjeljak

# a) TODO: učitaj i pogledaj kolone
df = pd.read_csv(FAJL)

print(df.columns)
print(df.shape)

# b) TODO: čišćenje
df["iznos"] = pd.to_numeric(df["iznos"], errors="coerce")
df["datum_vrijeme"] = pd.to_datetime(df["datum_vrijeme"], errors="coerce")

print("Neispravni iznosi:", df["iznos"].isna().sum())
print("Neispravni datumi:", df["datum_vrijeme"].isna().sum())

df = df.dropna(subset=["iznos", "datum_vrijeme"])

print(df.shape)

# c) TODO: izvedene kolone sat, dan, mjesec
df["sat"] = df["datum_vrijeme"].dt.hour
df["dan"] = df["datum_vrijeme"].dt.dayofweek.map(lambda x: DANI[x])
df["mjesec"] = df["datum_vrijeme"].dt.month

# d) TODO: top 5 gradova + grafikon
gradovi = df["grad"].value_counts().head(5)

print(gradovi)

gradovi.plot(kind="bar")
plt.title("Top 5 gradova po broju narudžbi")
plt.xlabel("Grad")
plt.ylabel("Broj narudžbi")
plt.tight_layout()
plt.savefig(os.path.join(FOLDER, "z4_gradovi.png"))
plt.show()

# e) TODO: narudžbe po satu + grafikon
sati = df["sat"].value_counts().sort_index()

print(sati)
print("Najviše narudžbi ima u:", sati.idxmax(), "h")

sati.plot(kind="bar")
plt.title("Broj narudžbi po satu")
plt.xlabel("Sat")
plt.ylabel("Broj narudžbi")
plt.tight_layout()
plt.savefig(os.path.join(FOLDER, "z4_sati.png"))
plt.show()

# f) TODO: prosječan iznos po kategoriji
kategorije = df.groupby("kategorija")["iznos"].mean().sort_values(ascending=False)

print(kategorije)

# BONUS
po_danu = df["dan"].value_counts().reindex(DANI)

print("Narudžbe po danima:")
print(po_danu)

print("Najjači dan:", po_danu.idxmax())

print("Ukupan promet:", round(df["iznos"].sum(), 2), "KM")
print("Prosječna narudžba:", round(df["iznos"].mean(), 2), "KM")

# BONUS 2
IZLAZ = os.path.join(FOLDER, "izvjestaj_narudzbe.xlsx")

with pd.ExcelWriter(IZLAZ) as pisac:
    gradovi.to_frame("broj_narudzbi").to_excel(pisac, sheet_name="Gradovi")
    kategorije.to_frame("prosjek_iznosa").to_excel(pisac, sheet_name="Kategorije")
    sati.to_frame("broj_narudzbi").to_excel(pisac, sheet_name="Sati")

print("Zadatak 4 - dopuni TODO dijelove.")
