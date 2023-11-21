mot = str(input("Entrez un mot sans espace: "))

while(" " in mot):
    mot = str(input("Vous avez entrez un mot avec des espaces, recommencez: "))

print("Merci, vous avez respecté la consigne.")