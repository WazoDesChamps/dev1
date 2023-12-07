import random

def liste_entiers_aléatoires(n, nmin, nmax):
    return [random.randint(nmin, nmax) for i in range(n)]

n = 15
nmin = 0
nmax = 100

print(liste_entiers_aléatoires(n, nmin, nmax))