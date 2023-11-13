import textwrap 

def nom_du_mois(mois):
    match mois:
        case 1:
            return "Janvier"
        case 2:
            return"Février"
        case 3:
            return"Mars"
        case 4:
            return"Avril"
        case 5:
            return"Mai"
        case 6:
            return"Juin"
        case 7:
            return"Juillet"
        case 8:
            return"Aout"
        case 9:
            return"Septembre"
        case 10:
            return"Octobre"
        case 11:
            return"Novembre"
        case 12:
            return"Décembre"
        
def afficher_titre(mois, annee):
    print(20*'=')
    return "     " + str(nom_du_mois(mois)) + " " + str(annee)

def est_bissextile(annee):
    return ((annee%4 == 0) and (annee%100 != 0) or annee%400 == 0)

def suite_numeros_jours(mois ,annee):
    if(est_bissextile(annee) and mois == 2):
        print("01 02 03 04 05 06 07\n08 09 10 11 12 13 14\n15 16 17 18 19 20 21\n22 23 24 25 26 27 28\n29")
    else:
        print("01 02 03 04 05 06 07\n08 09 10 11 12 13 14\n15 16 17 18 19 20 21\n22 23 24 25 26 27 28\n29 30 31")
 
def numero_jour(jour, mois, annee):
    q = jour
    m = mois
    J = annee/100
    K = annee%100
    h = (q + (((m + 1)*13) / 5) + K + (K / 4) + (J / 4) + 5 * J + 5)%7
    return int(h)