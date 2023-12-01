import time  

# Ajout des 5_000_000 de valeurs
a_list = []
total_time = 0

# Création de la liste
for i in range(5_000_000):
    a_list.append(i)

for k in range(50):
    value = 0
    # Calcul de la somme des éléments dans la liste
    start_time = time.time()  
    for j in range(len(a_list)):
        value = value + a_list[j]
    end_time = time.time()
    access_time = end_time - start_time
    print(value, access_time)

    total_time += access_time

# Calcul du temps moyen
average = total_time / 50
print("Average:", average, "s")
