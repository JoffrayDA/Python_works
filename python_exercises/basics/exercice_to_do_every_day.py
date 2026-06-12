fruits = ["Pomme", "Kiwi", "Poire", "Banane", "Goyave", "Prune", "Fraise", "Framboise", "Myrtille", "Figue", "Mangue", "Fruit de la Passion"]
# Fonctions Python de base 
# Imprime
print(fruits)
# Type d'une variable
print(type(fruits))
    # Nombre d'éléments
print(len(fruits))
    # Demander une saisie utilisateur
fruit_prefere = input ("Quel est ton fruit préféré ? ")
    # Créer une suite de nombres 
print(list(range(10,1)))
    # Méthode de liste
    # Ajoute un élément
fruits.append("Goyave")
    # Retire un élément 
fruits.remove("Pomme")
    # Supprime le dernier élément 
fruits.pop()
    # Trier la liste
fruits.sort()
    # Trouver la position d'un élément 
i_banane = fruits.index("Banane")
print(i_banane)
    # Chaine de caractères
mot = "Python"
    # Met en majuscule
majuscule = mot.upper()
minuscule = mot.lower()
    # Remplace un texte 
new_word = mot.replace("Bi", "Py")
    # Découpe en liste 
phrase = "Pomme,Kiwi,Poire"
liste_decoupee = phrase.split(",") # Donne ['Pomme', 'Kiwi', 'Poire']
print(liste_decoupee)
    # Fusionne une liste en texte 
fusion_txt = ", ".join(fruits)
print(fusion_txt)
    # Supprime les espaces début ou fin 
phrase_avec_espaces = "   Bonjour   "
phrase_propre = phrase_avec_espaces.strip()
