print("---Exercice1---")
profile = {
    "name": "Alice",
    "city": "Paris",
    "age": 30
}

# Affiche la ville
print("ville :", profile["city"])

print("---Exercice2---")
movie = {
    "title": "Inception",
    "year": 2010,
    "rating": 8.8
}

# Parcours le dictionnaire
# et affiche : clé -> valeur
for key, values in movie.items() : 
    print(key, "->", values)

print("---Exercice3---")
scores = {
    "player1": 12,
    "player2": 7
}

# Ajoute 5 points à player1
# Affiche le dictionnaire

scores["player1"] = scores["player1"] + 5
print(scores)

print("---Exercice4---")
colors = ["red", "blue", "red", "green", "blue", "red"]

# Crée un dictionnaire
# qui compte combien de fois chaque couleur apparaît

count = {}
for c in colors : 
    if c in count :
        count[c] += 1
    else : 
        count[c] = 1
print(count)

print("---Exercice5---")
prices = {
    "apple": 2,
    "banana": 1,
    "cherry": 4
}

# Parcours le dictionnaire
# et affiche seulement les fruits
# dont le prix est >= 2

for name, price in prices.items() : 
    if price >= 2 : 
        print(name)