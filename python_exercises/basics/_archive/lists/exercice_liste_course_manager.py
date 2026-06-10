courses = []

while True:
    choix = int(input("1 Ajouter / 2 Supprimer / 3 Voir / 4 Vider / 5 Quitter : "))

    if choix == 1:
        produit = input("Nom du produit : ")
        courses.append(produit)
    elif choix == 2:
        produit = input("Produit à retirer : ")
        if produit in courses:
            courses.remove(produit)
        else:
            print("Produit introuvable.")
    elif choix == 3:
        print("Liste actuelle :", courses)
    elif choix == 4:
        courses.clear()
        print("Liste vidée.")
    elif choix == 5:
        print("Au revoir 👋")
        break

