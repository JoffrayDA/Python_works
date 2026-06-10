print("---Exercice1---")
order = {
    "id": 501,
    "customer": "Marie",
    "total": 89.90
}
# Affiche le total de la commande
print("Montant total de la commande : ",order["total"],"€.")

print("---Exercice2---")
city = {
    "name": "Lyon",
    "population": 520000,
    "country": "France"
}

# Parcours le dictionnaire
# et affiche : clé -> valeur
for key, values in city.items():
    print(key, "->", values)

print("---Exercice3---")
budget = {
    "rent": 800,
    "food": 250
}

# Ajoute 50 au budget food
# Affiche le dictionnaire
budget["food"] = budget["food"] + 50
print(budget)

print("---Exercice4---")
results = ["win", "loss", "win", "draw", "win", "loss"]

# Crée un dictionnaire
# qui compte combien de fois chaque résultat apparaît
count = {}
for r in results : 
    if r in count : 
        count[r] += 1 
    else : 
        count[r] = 1
print(count)

print("---Exercice5---")
ratings = {
    "movie1": 7,
    "movie2": 9,
    "movie3": 6,
    "movie4": 8
}

# Parcours le dictionnaire
# et affiche seulement les films
# dont la note est >= 8
for m, n in ratings.items() :
    if n >= 8 : 
        print(m)