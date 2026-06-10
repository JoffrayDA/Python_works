courses = []

while True : 
    print("Liste de courses")
    print("1. Ajouter un produit: ")
    print("2. Retirer un produit: ")
    print("3. Afficher la liste: ")
    print("4. Chercher un produit: ")
    print("5. Effacer la liste: ")
    print("6. Trier la liste: ")
    print("7. Stop")
    
    choix = int(input("Ton choix : "))

    if choix == 1 : 
        produit = input("Quel produit voulez-vous ajouter ? :")
        courses.append(produit)
        print("Produit ajouté à la liste.")
    elif choix == 2 :
        produit = input("Quel produit voulez-vous retirer ?")
        if produit in courses :
            courses.remove(produit)
            print("Produit retiré.")
        else : 
            print("Ce produit n'est pas dans la liste.")
    elif choix == 3 : 
        print(courses)
    elif choix == 4 : 
        recherche = input("Quel produit recherchez-vous ?:")
        if recherche in courses :
            print(f"{recherche} est bien dans la liste.")
        else : 
            print("Ce produit n'est pas dans la liste.")
    elif choix == 5 : 
        courses.clear()
        print("La liste est bien effacée.")
        print(courses)
    elif choix == 6 : 
        courses.sort()
        print("La liste de course est bien triée.")
        print(courses)
    elif choix == 7 : 
        print("Courses fini.")
        break