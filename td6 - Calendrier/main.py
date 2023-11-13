import calendrier

jour = int(input("Jour: "))
mois = int(input("Mois: "))
annee = int(input("Année: "))

print(calendrier.afficher_titre(mois, annee))
print(20*'=')

calendrier.suite_numeros_jours(mois,annee)

suite_numeros = 3 * calendrier.numero_jour(jour, mois, annee)
