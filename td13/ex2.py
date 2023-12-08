#Dictionnaires
profs_dev1 = {
    "A111": "bej", "A112": "mbr", "A121": "sre", "A122": "dbo", "A131": "abe",
    "A132": "clg", "A211": "bej", "A212": "cuv", "A221": "sre", "A222": "sdr",
    "A231": "hal", "A232": "nri", "A311": "bis", "A312": "clg", "A321": "cuv",
    "A322": "hal", "A331": "srv", "A332": "gba", "A341": "pbt", "A342": "tni"
}

etudiants = {
    52104: {
        "prénom": "Guillaume",
        "nom": "Apollinaire",
        "groupe": "A321"
    },
    45371: {
        "prénom": "Jean-Jacques",
        "nom": "Goldmann",
        "groupe": "A123"
    }
}

# obtenir le prof du groupe A311
for k in profs_dev1:
    if k == "A311":
        print(profs_dev1[k])

#▷ obtenir le nombre de groupes de Mme Cuvelier (cuv).
cpt = 0
for k, v in profs_dev1.items():
    if v == "mbr":
        cpt += 1

print("cuv a", cpt, "groupe.")

#▷ obtenir le groupe de l’étudiant ayant le matricule 52104
print(etudiants.get(52104, {}).get("groupe", {}))

#▷ afficher tou·tes les enseignant·es de dev1 (sans doublons)
print(set(profs_dev1.values()))