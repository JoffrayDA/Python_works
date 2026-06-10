print("---Exercice1---")
user = {
    "username": "pierre26",
    "age": 26,
    "country": "France"
}

# Affiche l'âge de l'utilisateur

print("Âge utilisateur :",user["age"])

print("---Exercice2---")
car = {
    "brand": "Toyota",
    "year": 2018,
    "price": 15000
}

# Parcours le dictionnaire
# et affiche : clé -> valeur

for key, values in car.items() : 
    print(key, "->", values)

print("---Exercice3---")

stock = {
    "apple": 10,
    "banana": 5
}

# Ajoute 3 pommes au stock
# Affiche le dictionnaire mis à jour
stock["apple"] = stock["apple"] + 3
print(stock)

print("---Exercice4---")
letters = ["x", "y", "x", "z", "y", "x"]

# Crée un dictionnaire
# qui compte combien de fois chaque lettre apparaît
count = {}
for l in letters :
    if l in count :
        count[l] +=1
    else :
        count[l] =1
print(count)

print("---Exercice5---")
grades = {
    "math": 14,
    "english": 9,
    "history": 12
}

# Parcours le dictionnaire
# et affiche seulement les matières
# où la note est >= 10

for subject, grade in grades.items():
    if grade >= 10:
        print(subject)
