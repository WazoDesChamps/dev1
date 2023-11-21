import random

nb_random = random.randint(0, 10)

val = int(input("Val: "))

while(val != nb_random):
    val = int(input("Valeur non trouvé:"))

print("ok")