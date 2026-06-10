print("---Exercice1---")
account = {
    "id": 1024,
    "owner": "Pierre",
    "balance": 2500
}

# Affiche le solde du compte

print("Solde du compte :",account["balance"])

print("---Exercice2---")
book = {
    "title": "1984",
    "author": "George Orwell",
    "year": 1949
}

# Parcours le dictionnaire
# et affiche : clé -> valeur

for k, v in book.items() : 
    print(k, "->", v)

print("---Exercice3---")
inventory = {
    "pen": 20,
    "notebook": 5
}

# Ajoute 10 stylos ("pen") au stock
# Affiche le dictionnaire

inventory["pen"] = inventory["pen"] + 10
print(inventory)

print("---Exercice4---")
animals = ["cat", "dog", "cat", "bird", "dog", "cat"]

# Crée un dictionnaire
# qui compte combien de fois chaque animal apparaît

count = {}
for c in animals : 
    if c in count : 
        count[c] += 1
    else : 
        count[c] = 1
print(count)

print("---Exercice5---")
temps = {
    "Paris": 18,
    "London": 12,
    "Madrid": 25,
    "Berlin": 9
}

# Parcours le dictionnaire
# et affiche seulement les villes
# où la température est > 15

for c, t in temps.items() : 
    if t > 15 : 
        print(c)