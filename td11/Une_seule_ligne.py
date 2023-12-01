#Ajout des différents modules
import random

##########################
#Declartion des variables#
##########################

#Création de notre liste plateau
_plateau = []

#Ajout des 20 cases dans le plateau
for i in range(20):
    _plateau.append(0)

#Valeurs possibles à utiliser durant la partie
_valeurs = random.randint(0, 4)

#########################
#Fonctions et programme #
#########################

#Ajoute 2 valeurs aléatoire sur le plateau
def add_2_values():
    _pos_1 = random.randint(0, 20)
    while(_plateau[_pos_1] != 0):
        _pos_1 = random.randint(0, 20)

    _pos_2 = random.randint(0, 20)
    while(_plateau[_pos_2] != 0):
        _pos_2 = random.randint(0, 20)

    _plateau.insert(_pos_1, _valeurs)
    _plateau.insert(_pos_2, _valeurs)