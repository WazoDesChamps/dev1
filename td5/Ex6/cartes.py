import random

def hasard(x, y:
    return random.randint(x, y

def tirer_carte(:
    les_valeurs = [2,3,4,5,6,7,8,9,10,'valet','dame','roi','as']
    les_couleurs = ['pique','trèfle','cœur','carreau']

    lenght_valeurs = len(les_valeurs
    lenght_couleurs = len(les_couleurs

    valeurs = les_valeurs[hasard(0, lenght_valeurs - 1]
    couleurs = les_couleurs[hasard(0, lenght_couleurs - 1]

    return ([valeurs, couleurs]