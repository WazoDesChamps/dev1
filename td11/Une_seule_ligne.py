# Ajout des différents modules
import random

##########################
# Declaration des variables
##########################

# Création de notre liste plateau
_plateau = []

# Ajout des 20 cases dans le plateau
for i in range(20):
    _plateau.append(0)

#########################
# Fonctions et programme
#########################

# Ajoute 2 valeurs aléatoires sur le plateau
def add_2_values():
    _pos_1 = random.randint(0, 19)
    while _plateau[_pos_1] != 0:
        _pos_1 = random.randint(0, 19)

    _plateau[_pos_1] = random.randint(1, 5)

    _pos_2 = random.randint(0, 19)
    while _plateau[_pos_2] != 0:
        _pos_2 = random.randint(0, 19)

    _plateau[_pos_2] = random.randint(1, 5)


# Permet d'afficher le plateau
def display():
    print("Plateau :", _plateau)

# Permet de déplacer une valeur d'un point A à un point B
def move(origin, destination):
    if 1 or 2 or 3 or 4 not in _plateau[origin - 1 : destination]:
        print("Règle non respectée, il y a des valeurs entre l'origine et la destination.")
    else:
        _plateau[destination - 1] = _plateau[origin - 1]
        _plateau[origin - 1] = 0

# Lit les valeurs encodées par l'utilisateur
def read():
    _origin_val = int(input("Entrez une valeur d'origine (1-20) : "))
    _dest_val = int(input("Entrez une valeur de destination (1-20) : "))

    move(_origin_val, _dest_val)

#Supprime si il y a 3 même valeurs cote à cote
def remove_3_inline():
    i = 0
    while(i < len(_plateau) - 2):
        if ((_plateau[i] == _plateau[i + 1] == _plateau[i + 2]) and _plateau[i] != 0):
            del _plateau[i: i + 3]
            _plateau.insert(i, 0)
            _plateau.insert(i + 1, 0)
            _plateau.insert(i + 2, 0)
        else:
            i += 1

# Fonction principale
def main():
    tours_joues = 0
    while 0 in _plateau or len(_plateau) < 20:
        add_2_values()
        display()
        read()
        remove_3_inline()
        tours_joues += 1

    print("Nombre de tours joués :", tours_joues)

if __name__ == "__main__":
    main()