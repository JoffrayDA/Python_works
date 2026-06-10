print("---Exercice1---")
employee = {
    "name": "Luc",
    "department": "Sales",
    "salary": 3200
}

# Affiche le salaire
print("Salaire :", employee["salary"])

print("---Exercice2---")
phone = {
    "brand": "Samsung",
    "model": "S23",
    "price": 899
}

# Parcours le dictionnaire
# et affiche : clé -> valeur
for key, values in phone.items() : 
    print(key, "->", values)

print("---Exercice3---")
cart = {
    "apple": 2,
    "banana": 4
}

# Ajoute 1 pomme au panier
# Affiche le dictionnaire
cart["apple"] = cart["apple"] + 1
print(cart)

print("---Exercice4---")
votes = ["yes", "no", "yes", "yes", "no"]

# Crée un dictionnaire
# qui compte combien de fois chaque vote apparaît
count = {}

for v in votes : 
    if v in count : 
        count[v] += 1 
    else : 
        count[v] = 1
print(count)

print("---Exercice5---")
scores = {
    "Alice": 15,
    "Bob": 8,
    "Charlie": 11
}

# Parcours le dictionnaire
# et affiche seulement les prénoms
# dont le score est >= 10
for name, s in scores.items() : 
    if s >= 10 : 
        print(name)
