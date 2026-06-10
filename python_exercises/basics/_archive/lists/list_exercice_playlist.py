chansons = []
import random

while True : 
    choix = int(input("1 - Ajouter / 2 - Retirer / 3 - Afficher / 4 - Mélanger l'ordre / 5 - Vider / 6 - Quitter :"))

    if choix == 1: 
        musique = input("Nom de la chanson :")
        chansons.append(musique)
    elif choix == 2: 
        musique = input("Tu veux retirer quelle musique ? : ")
        if musique in chansons : 
            chansons.remove(musique)
        else : 
            print("Cette chanson n'est pas dans la liste.")
    elif choix == 3:
        print(chansons)
    elif choix == 4:
        random.shuffle(chansons)
        print(chansons)
    elif choix == 5 : 
        chansons.clear()
    elif choix == 6:
        print("Adios")
        break