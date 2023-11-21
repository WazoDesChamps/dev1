while True:
    mot = input("Entrez un mot: ")
    premire_lettre = mot[0];
    derniere_lettre = mot[len(mot-1)]

    if premire_lettre == derniere_lettre:
        print ("Même lettre.")

    else:
        print ("Pas la même.")
