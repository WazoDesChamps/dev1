def addition(l1, valeur):
    return [i * valeur for i in l1]

ma_liste = [x for x in range(25) if x**2 <= 25]

print(addition(ma_liste, 2))