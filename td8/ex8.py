val = int(input("Nombre de passager: "))

for i in range(val):
    nom = str(input("Quel est votre nom: "))
    poids_valise = int(input("Quel est le poids de votre valise: "))
    if(poids_valise > 10):
        print("Votre valise est trop lourde, vous allez de voir payer un supplément.")