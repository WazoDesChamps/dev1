val = int(input("Encodez une valeur pour le triangle pointe inversé: "))

for i in range(val + 1, 0, -1):
    ligne = i * "*"
    for j in range(val + 1, 0, 1):
        print(i * "*")