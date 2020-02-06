#Ce code permet de déterminer si une année (quelconque) est bissextile.

annee = input("Saissisez une année")

try:
    annee = int(annee)
    
except:
    print("Erreur lors de la conversion de l'année")
    
finally:
    print("Vous avez choisi l'année suivante:", annee)
    if annee%4 == 0:
        print(annee, "n'est pas une année bissextile")
    elif  annee%4 == 0:
        if annee%100!=0:
            print(annee, "est une année bissextile")
        else:
            if annee%400==0:
                print(annee, "est une année bissextile")
            else:
                print(annee, "n'est pas une année bissextile") 

