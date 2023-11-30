import time

#Ajout des 5_000_000 de valeurs
a_tuple = ()
total_time = 0

for i in range(5_000_000):
    a_tuple = a_tuple + (i,)

for k in range(50):
    value = 0
    #calcul de la somme des éléments dans le tuple
    start_time = time.time() 
    for j in range(len(a_tuple)):
        value = value + a_tuple[j]
    end_time = time.time()
    acces_time = end_time - start_time
    print(value, acces_time)

    total_time += acces_time

#Calcul du temps moyen
average = total_time / 50
print("Average:", average,"s")