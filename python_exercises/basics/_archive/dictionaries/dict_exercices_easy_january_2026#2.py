print("Exercice1---Le Menu du Resto")
menu = {"Pizza": 12, "Burger": 10, "Salade": 8}

for plat, prix in menu.items() : 
    print(plat, ":", prix )
print("--------------------------")


print("Exercice2---Le Prof de Maths")
notes = {"Alice": 15, "Bob": 12, "Charlie": 18}

moyenne = sum(notes.values()) / len(notes.values())
print("La moyenne des notes est de :", moyenne)
print("--------------------------")


print("Exercice3---Inventaire de Gamer")
inventaire = {"épée": 1, "potions": 3, "pièces": 50}

if "pièces" in inventaire : 
    inventaire["pièces"] += 25
else : 
    inventaire["pièces"] = 25
print(inventaire)
print("--------------------------")


print("Exercice4---Traducteur Simple")
couleurs = {"red": "rouge", "blue": "bleu", "green": "vert"}
mot = input("Donne moi un mot anglais :" )

if mot in couleurs : 
    print(couleurs[mot])
else : 
    print("je ne connais pas ce mot")
print("--------------------------")


print("Exercice5---Suppression d'Intrus")
data = {"id": 1, "temp": 22, "error": "None"}

del data["error"]
print(data)








