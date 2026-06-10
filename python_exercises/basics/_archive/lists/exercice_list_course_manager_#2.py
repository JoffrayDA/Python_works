courses = []

while True :
    print("\n Liste de Course")
    print("1. Ajouter produit")
    print("2. Supprimer produit")
    print("3. Afficher la liste")
    print("4. Trier la liste")
    print("5. Chercher dans la liste")
    print("6. Quitter")

    choix = int(input("Quel est ton choix ? :"))

    if choix == 1 :
        produit = input("Quel produit veux-tu ajouter? :")
        courses.append(produit)
    elif choix == 2 : 
        produit = input("Quel produit veux-tu retirer? :")
        if produit in courses : 
            courses.remove(produit)
        else : 
            print("Ce produit n'est pas dans la liste de courses.")
    elif choix == 3 : 
        print(courses)
    elif choix == 4 : 
        courses.sort()
        print(courses)
    elif choix == 5 : 
        recherche = input("Quel produit cherches-tu ?:")
        if recherche in courses :
            print(f"{recherche} est bien dans la liste de course !")
        else : 
            print(f"{recherche} n'est pas dans la liste de course.")
    elif choix == 6 : 
        print("A bientôt")
        break