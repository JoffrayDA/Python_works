print("Exercice1---La Liste de Courses")
courses = ["Pain", "Lait", "Oeufs", "Crevettes"]

courses.append("Fromage")
print("Premier élément liste de courses :", courses[0])
print(courses)
print("--------------------------")


print("Exercice2---Changement de Plan")
villes = ["Paris", "Lyon", "Marseille"]

villes[1] = "Bordeaux"
print(villes)
print("--------------------------")


print("Exercice3---Somme de deux nombres")
nombres = [10, 20, 30, 40]

resultat = nombres[0] + nombres[-1]
print("Resultat du premier et du dernier nombre :", resultat)
print("--------------------------")


print("Exercice4---Vérification d'invité")
amis = ["Alice", "Bob", "Charlie"]

nom = "Bob"

def invitation(): 
    if nom in amis :
        print("Bob est invité !")
    else : 
        print("Bob n'est pas invité.")

invitation()
print("--------------------------")


print("Exercice5---Compter les éléments")
couleurs = ["rouge", "vert", "bleu", "jaune", "orange"]
nb_couleurs = len(couleurs)

print(f"Il y a {nb_couleurs} couleurs dans la liste.")