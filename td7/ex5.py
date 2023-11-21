import random

nb_random = random.randint(1, 10)
compteur = 1
print(nb_random)

val = int(input("Trouvez une valeur entre 1 et 10: "))

while(val != nb_random and val > 0):
    val = int(input("Raté ! Recommencez: "))
    compteur += 1

print("Bravo vous avez trouvé en " + str(compteur) + " essais.")