cpt = 0

val = int(input("Entrez une suite de nombre et terminez par -1: "))
total = 0
moyenne = 0

while(val > -1):
    cpt += 1
    total += val
    val = int(input("Entrez une autre valeur et terminez par -1: "))

moyenne = total/cpt 
print("La moyenne des nombres que vous avez entré est de ", moyenne)
