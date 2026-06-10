print("---Exercice1---")
students = {
    "Alice": [12, 14, 15],
    "Bob": [9, 10, 8],
    "Charlie": [16, 17, 15]
}

# Affiche la moyenne de chaque étudiant
for key, values in students.items() : 
    average = sum(values) / len(values)
    print(key, "->", average)

print("---Exercice2---")
products = {
    "laptop": 1200,
    "mouse": 25,
    "keyboard": 80,
    "screen": 300
}

# Affiche seulement les produits
# dont le prix est > 100
for product, price in products.items() : 
    if price > 100 : 
        print(product)

print("---Exercice3---")
ages = [18, 21, 17, 30, 25, 16, 40]

# Crée un dictionnaire avec :
# "adult" : nombre de personnes >= 18
# "minor" : nombre de personnes < 18
count = {
    "adult" : 0,
    "minor" : 0
}

for a in ages : 
    if a >= 18 : 
        count["adult"] += 1
    else : 
        count["minor"] += 1
print(count)

print("---Exercice4---")
users = {
    "user1": {"age": 25, "active": True},
    "user2": {"age": 17, "active": False},
    "user3": {"age": 30, "active": True}
}

# Affiche seulement les utilisateurs
# qui sont actifs
for name, info in users.items():
    if info["active"] == True:
        print(name)

print("---Exercice5---")
sales = {
    "January": 1200,
    "February": 950,
    "March": 1430,
    "April": 800
}

# Affiche les mois
# où les ventes sont >= 1000

for m, s in sales.items() :
    if s >= 1000 : 
        print(m)