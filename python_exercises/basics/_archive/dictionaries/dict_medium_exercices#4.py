print("---Exercice1---")
invoice = {
    "number": 2025,
    "client": "ACME",
    "amount": 430
}

# Affiche le montant de la facture
print("Montant de la facture : ", invoice["amount"], "€.")

print("---Exercice2---")
student = {
    "name": "Emma",
    "age": 22,
    "city": "Bordeaux"
}

# Parcours le dictionnaire
# et affiche : clé -> valeur
for key, value in student.items():
    print(key, "->", value)

print("---Exercice3---")
scores = {
    "teamA": 10,
    "teamB": 14
}

# Ajoute 3 points à teamA
# Affiche le dictionnaire
scores["teamA"] = scores["teamA"] + 3
print(scores)

print("---Exercice4---")
messages = ["sent", "received", "sent", "sent", "received"]

# Crée un dictionnaire
# qui compte combien de fois chaque statut apparaît
count = {}

for m in messages : 
    if m in count : 
        count[m] += 1 
    else : 
        count[m] = 1 
print(count)

print("---Exercice5---")
countries = {
    "France": 67,
    "Germany": 83,
    "Spain": 47,
    "Italy": 60
}

# Parcours le dictionnaire
# et affiche seulement les pays
# dont la population est >= 60
for c, p in countries.items():
    if p >= 60 : 
        print(c)