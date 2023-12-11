from collections import defaultdict

profs_dev1 = {
    "A111": "bej", "A112": "mbr", "A121": "sre", "A122": "dbo", "A131": "abe",
    "A132": "clg", "A211": "bej", "A212": "cuv", "A221": "sre", "A222": "sdr",
    "A231": "hal", "A232": "nri", "A311": "bis", "A312": "clg", "A321": "cuv",
    "A322": "hal", "A331": "srv", "A332": "gba", "A341": "pbt", "A342": "tni"
}

# Create a defaultdict to store the number of occurrences for each value
occurrences = defaultdict(int)

# Iterate through the values of the original dictionary
for value in profs_dev1.values():
    # Increment the occurrence count for each value
    occurrences[value] += 1

# Create a new dictionary with unique values and their occurrence count
unique_profs_dev1 = {key: {'value': value, 'occurrences': occurrences[value]} for key, value in profs_dev1.items()}

# Print the new dictionary with unique values and their occurrence count
print(unique_profs_dev1)
