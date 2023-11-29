total = int(input("Combien d'entier voulez vous encoder ? "))
premier = False

for i in range(1, total + 1, 1):
    print("Nous allons vérifier si votre entier est un nombre premier ou non.")
    val = int(input("Encoder votre nombre: "))
    for j in range(2, val + 1, 1):
        if(val%1 == 0 and val%val == 0 and val%j != 0):
            premier = True
    if premier:
        print("Nombre premier.")
    else:
        print("Nombre pas premier.")

