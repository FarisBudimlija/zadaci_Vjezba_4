# =============================================================
# ZADATAK 1: Izvještaj po smjeru (BEZ pandasa - samo modul csv)
# Uvod u analizu podataka - Vježbe, Sedmica 4
# =============================================================
# Fajl studenti.csv ima kolone:
#   ime,smjer,godina,matematika,programiranje,statistika,prisustvo
#
# a) Učitaj fajl u LISTU RJEČNIKA (csv.DictReader). Kolone godina,
#    matematika, programiranje, statistika i prisustvo pretvori u int.
#
# b) Svakom studentu dodaj ključ "prosjek":
#       (matematika + programiranje + statistika) / 3
#
# c) Grupiši studente po smjeru: rječnik u kojem je ključ smjer,
#    a vrijednost lista studenata tog smjera.
#
# d) Za svaki smjer izračunaj: broj studenata, prosjek smjera
#    (prosjek prosjeka) i najboljeg studenta. Ispiši smjerove
#    sortirane po prosjeku OPADAJUĆE, tačno ovako:
#
#    Informatika: 14 studenata, prosjek 8.10, najbolji: Ema (9.00)
#    Elektrotehnika: 14 studenata, prosjek 7.29, najbolji: Dino (8.33)
#    Menadžment: 12 studenata, prosjek 7.00, najbolji: Lana (7.67)
#
#    Savjet: max(lista, key=lambda s: s["prosjek"])
#            sorted(..., key=lambda r: r["prosjek"], reverse=True)
#
# e) Upiši izvještaj u fajl "izvjestaj_smjerovi.csv" sa kolonama:
#       smjer,broj_studenata,prosjek,najbolji
#    Savjet: csv.DictWriter, writeheader(), writerow()
#
# BONUS: napiši funkciju polozio(student) koja vraća True ako su sve
#        tri ocjene >= 6. Koliko je studenata položilo?  (očekivano: 25)
# =============================================================
import csv
import os

FOLDER = os.path.dirname(os.path.abspath(__file__))
FAJL = os.path.join(FOLDER, "studenti.csv")
IZLAZ = os.path.join(FOLDER, "izvjestaj_smjerovi.csv")

# a) TODO: učitaj studente u listu rječnika
studenti = []

with open(FAJL, "r", encoding="utf-8") as f:
    citac = csv.DictReader(f)
    for red in citac:
        student = {
            "ime": red["ime"],
            "smjer": red["smjer"],
            "godina": int(red["godina"]),
            "matematika": int(red["matematika"]),
            "programiranje": int(red["programiranje"]),
            "statistika": int(red["statistika"]),
            "prisustvo": int(red["prisustvo"])
        }

        studenti.append(student)


print("Učitano studenata:", len(studenti))      # očekivano: 40

# b) TODO: dodaj ključ "prosjek" svakom studentu
for student in studenti:
    student["prosjek"] = (
        student["matematika"] +
        student["programiranje"] +
        student["statistika"]
    ) / 3

# c) TODO: grupiši po smjeru
po_smjeru = {}

for student in studenti:
    smjer = student["smjer"]

    if smjer not in po_smjeru:
        po_smjeru[smjer] = []

    po_smjeru[smjer].append(student)

# d) TODO: izvještaj za svaki smjer, sortiran po prosjeku opadajuće
izvjestaj = []

for smjer, lista_studenata in po_smjeru.items():

    broj = len(lista_studenata)

    prosjek = sum(
        s["prosjek"] for s in lista_studenata
    ) / broj

    najbolji = max(
        lista_studenata,
        key=lambda s: s["prosjek"]
    )
    red = {
        "smjer": smjer,
        "broj_studenata": broj,
        "prosjek": prosjek,
        "najbolji": najbolji["ime"]
    }
    izvjestaj.append(red)

izvjestaj = sorted(
    izvjestaj,
    key=lambda r: r["prosjek"],
    reverse=True
)

for red in izvjestaj:

    najbolji = max(
        po_smjeru[red["smjer"]],
        key=lambda s: s["prosjek"]
    )

    print(
        f'{red["smjer"]}: {red["broj_studenata"]} studenata, '
        f'prosjek {red["prosjek"]:.2f}, '
        f'najbolji: {najbolji["ime"]} ({najbolji["prosjek"]:.2f})'
    )

# e) TODO: upiši izvještaj u izvjestaj_smjerovi.csv
with open(IZLAZ, "w", newline="", encoding="utf-8") as f:

    kolone = ["smjer", "broj_studenata", "prosjek", "najbolji"]

    pisac = csv.DictWriter(f, fieldnames=kolone)

    pisac.writeheader()

    for red in izvjestaj:
        pisac.writerow({
            "smjer": red["smjer"],
            "broj_studenata": red["broj_studenata"],
            "prosjek": f'{red["prosjek"]:.2f}',
            "najbolji": red["najbolji"]
        })

# BONUS: TOD
def polozio(student):
    return False
