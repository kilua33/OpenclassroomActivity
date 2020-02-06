import os
from random import randrange
from math import ceil

#Déclaration des variables de départ
argent = 1000 
continuer_partie = True

print("Vous vous installez à la table avec", argent, "$")

while continuer_partie:
    nombre_mise = -1
    while nombre_mise < 0 or nombre_mise > 49:
        nombre_mise  = input("Veuillez choisir un nombre compris entre 0 et 49 sur lequel vous voulez miser: ")
        try:
            nombre_mise = int(nombre_mise)
        except ValueError:
            print("Vous n'avez pas saisi de nombre")  
            nombre_mise = -1
            continue
        if nombre_mise<0 or nombre_mise>49:
            print("Le nombre que vous avez saisi n'est pas valide") 

    mise =0
    while mise<=0 or mise>1000:
        mise = input("Tapez le montant de votre mise ")
        try :
            mise=int(mise)
        except ValueError:
            print("Vous n'avez pas saisi de mise")
            mise=-1
            continue
        if mise<=0:
            print("Vous n'avez rien miser")
        if mise>argent:
            print("Vous ne pouvea pas miser plus que votre solde, il ne vous reste que", argent, "$")

    numero_gagnant=randrange(50)
    print("La roulette s'arrête sur le numero gagnant", numero_gagnant)

    #On établit les gains du jouer
    if numero_gagnant == nombre_mise:
        print("Féliciations, vous venez de gagner ", mise*3, "$")
        argent = argent +  mise*3
    elif numero_gagnant%2 == nombre_mise%2:
        mise=ceil(mise*0.5)
        print("Félicitations, vous avez misé sur la bonne couleur. Vous venez de gagner ",  mise, "$")
        argent= argent +mise*0.5
    else:
        argent=argent-mise
        print("Désolé mais vous venez de perdre", mise,"$")
        
    if argent<=0:
        print("Votre solde est tombé à zéro")
        continue_partie=False
    else:
        print("Il vous reste", argent, "$")
        quitter = input("Souhaitez vous quitter la table (o/n) ? ")
        if quitter == "o" or quitter == "O":
            print("Vous venez de quitter la table")
            continue_partie=False

os.system("pause")