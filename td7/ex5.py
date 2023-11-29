import random

nb_random = random.randint(1, 100)
compteur = 1

val = int(input("Trouvez une valeur entre 1 et 10: "))

while(val != nb_random and val > 0):
    val = int(input("Raté ! Recommencez: "))
    compteur += 1

print("Bravo vous avez trouvé en " + str(compteur) + " essais.")