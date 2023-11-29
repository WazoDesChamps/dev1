val = int(input("Entrez un entier pour la taille du carré : "))

for i in range(val):
    ligne = ""
    for j in range(val):
        ligne += "*"
    print(ligne)
