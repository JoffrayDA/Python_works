# --- BASE DE DONNÉES DU PROJET ---
# Format : [Titre, Score/10, Genre]
movies = [
    ["Inception", 8.8, "Science-Fiction"],
    ["The Godfather", 9.2, "Crime"],
    ["Toy Story", 8.3, "Animation"],
    ["The Dark Knight", 9.0, "Action"],
    ["Parasite", 8.6, "Drame"],
    ["Interstellar", 8.6, "Science-Fiction"]
]

print("--- Bienvenue dans MovieFilter Pro ---")

# MISSION 1 : Extraire uniquement les titres des films
# Utilise une list comprehension
titles = [m[0] for m in movies]
print(f"Liste des films disponibles : {titles}")
print("---------------------")

# MISSION 2 : Filtrer les films "Coup de Coeur"
# Crée une liste 'top_rated' qui contient les films ayant un score > 8.7
top_rated = []
for m in movies:
    if m[1] > 8.7 : 
        top_rated.append(m[0]) 
print(f"Liste des films ayant un meilleur score que 8.7 : {top_rated}")
print("---------------------")


# MISSION 3 : Recherche par genre
# Demande à l'utilisateur un genre, et affiche les films correspondants
search_genre =  input("Quel genre recherchez-vous ? :")
matching_movies = []

# A TON TOUR : Si le genre (indice 2) correspond à search_genre, 
# ajoute le titre à matching_movies
# ... ton code ici ...
for m in movies : 
    if m[2].lower() == search_genre.lower():
        matching_movies.append(m[0])

if matching_movies:
    print(f"Films trouvés en '{search_genre}' : {matching_movies}")
else:
    print(f"Désolé, aucun film trouvé pour le genre : {search_genre}")
print("-" * 30)

print("---------------------")

# MISSION 4 : Calculer la moyenne des scores
# Récupère tous les scores dans une liste 'all_scores' puis calcule la moyenne
# ... ton code ici ...
all_scores = [m[1] for m in movies ]
if len(all_scores) > 0 : 
    moyenne = sum(all_scores) / len(all_scores)
print(f"La note moyenne de notre catalogue est de : {round(moyenne, 2)}/10")

print("-" * 30)
print("Fin du programme. Merci d'avoir utilisé MovieFilter Pro !")