import random

print("Trouver le prix de l'objet X..")
prix = (random.randint(1,10))
for k in range (5):
    essai = int(input("Votre proposition entre 1 et 10 :"))
    if essai < 1 or essai > 10:
        print ("entrez un valeur entre 1 et 10")
    elif essai >= 1 and essai < prix :
        print ("Le prix est plus cher")
    elif essai <= 10 and essai > prix :
        print ("Le prix est moins cher")
    elif essai == prix :
        print ("Le prix est juste!!!",prix)
        break

print ("Le prix est ",prix)