profs_dev1 = {
    "A111": "bej", "A112": "mbr", "A121": "sre", "A122": "dbo", "A131": "abe",
    "A132": "clg", "A211": "bej", "A212": "cuv", "A221": "sre", "A222": "sdr",
    "A231": "hal", "A232": "nri", "A311": "bis", "A312": "clg", "A321": "cuv",
    "A322": "hal", "A331": "srv", "A332": "gba", "A341": "pbt", "A342": "tni"
}

# obtenir le prof du groupe A311
for k in profs_dev1:
    if k == "A311":
        prof = profs_dev1[k]
        break

print(profs_dev1[k])