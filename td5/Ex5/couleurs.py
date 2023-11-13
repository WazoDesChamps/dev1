import random

def hasard(x, y:
    return random.randint(x, y

def couleurs(:
    couleurs = ['rouge', 'vert', 'jaune', 'bleu', 'blanc', 'noir']
    nombre_couleurs = len(couleurs

    random_couleur = couleurs[hasard(0, nombre_couleurs - 1]
    return sorted([random_couleur]