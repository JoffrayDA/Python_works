print("---Exercice1---")
product = {
    "name": "Laptop",
    "price": 1200,
    "stock": 8
}
# Affiche le prix du produit
print("Prix :",product["price"],"€.")

print("---Exercice2---")
company = {
    "name": "TechCorp",
    "employees": 150,
    "country": "France"
}
# Parcours le dictionnaire
# et affiche : clé -> valeur
for key, value in company.items() : 
    print(key, "->", value)

print("---Exercice3---")
points = {
    "Alice": 5,
    "Bob": 3
}
# Ajoute 2 points à Alice
# Affiche le dictionnaire
points["Alice"] = points["Alice"] + 2
print(points)

print("---Exercice4---")
actions = ["click", "view", "click", "click", "view", "scroll"]

# Crée un dictionnaire
# qui compte combien de fois chaque action apparaît
count = {}
for a in actions : 
    if a in count : 
        count[a] += 1
    else : 
        count[a] = 1
print(count)

print("---Exercice5---")
grades = {
    "math": 12,
    "english": 9,
    "history": 15,
    "physics": 8
}

# Parcours le dictionnaire
# et affiche seulement les matières
# dont la note est >= 10
for m, g in grades.items() : 
    if g >= 10 : 
        print(m)

        