import time

#Ajout des 5_000_000 de valeurs
value = 0
a_tuple = ()
for i in range(5_000_000):
    a_tuple = a_tuple + (i,)

#calcul de la somme des éléments dans le tuple
start_time = time.time() 
for j in range(len(a_tuple)):
    value = value + a_tuple[j]
end_time = time.time()

#Calcul du temps
acces_time = end_time - start_time

print("Le temps pour calculer la somme de tous les éléments est de", acces_time)