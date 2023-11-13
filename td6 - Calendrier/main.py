import calendrier
import textwrap

mois = int(input("Mois: "))
annee = int(input("Année: "))

print(calendrier.afficher_titre(mois, annee) + "\n" + 20*'=')

suite_numeros = ((3 * calendrier.numero_jour(1, mois, annee)) * " " + calendrier.suite_numeros_jours(mois, annee))

print(textwrap.fill(suite_numeros, width=21))