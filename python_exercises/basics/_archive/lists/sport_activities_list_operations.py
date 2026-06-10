import numpy as np 

activites = ["course", "natation", "renforcement", "repos", "course"]

print("Longueur : ",len(activites))
print("Première activité :",activites[0])
print("Dernière activité :",activites[-1])
print("Trois premières activités :",activites[:3])

#Remplacer l'activité repos par yoga
activites[activites.index("repos")] = "yoga"

#Ajouter marche aux activités
activites.append("marche")

#Insérer vélo en deuxième position
activites.insert(2, "vélo")

#Afficher le nombre de "course"
print(activites.count("course"))

#Trouver l'index du mot "natation"
print([activites.index("natation")])

#Trier la liste dans l'ordre alphabétique

print(sorted(activites))
