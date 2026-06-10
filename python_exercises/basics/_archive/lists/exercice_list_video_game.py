import random 
jeux_videos = []


while True :
    choix = int(input("1 - Ajouter / 2 - Retirer / 3 - Afficher / 4 - Mélanger l'ordre / 5 - Vider / 6 - Quitter :"))

    if choix == 1 : 
        jeux = input("Quel jeux veux-tu ajouter ? :")
        jeux_videos.append(jeux)
        print(f"Ce {jeux} a bien été ajouté à la collection.")
    elif choix == 2 : 
        jeux = input("Quel jeux voulez vous retirer de la liste")
        if jeux in jeux_videos : 
            jeux_videos.remove(jeux)
            print(f"Ce {jeux} a bien été supprimé")
        else : 
            print(f"Ce {jeux} n'est pas dans la liste")
    elif choix == 3 : 
        print(jeux_videos)
    elif choix == 4 :
        random.shuffle(jeux_videos)
        print(jeux_videos)
    elif choix == 5 : 
        jeux_videos.clear()
        print(jeux_videos)
    else : 
        print("Adios")
        break


