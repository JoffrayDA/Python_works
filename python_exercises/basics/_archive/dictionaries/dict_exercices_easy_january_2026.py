print("Exercice1---Ta première fiche")
utilisateur = {
    "nom" : "Joffray",
    "age" : 25,
    "ville" : "Paris"
}

print(utilisateur["age"])
utilisateur["ville"] = "Lyon"
print(utilisateur) 
print("--------------------------")

print("Exercice2---Le Panier de Fruits")
stock = {"pommes": 10, "bananes": 5, "oranges": 8}
stock["pommes"] = 8 
stock["kiwi"] = 4
print(stock)
print("--------------------------")


print("Exercice3---Contact de secours")
repertoire = {"Police": 17, "Pompiers": 18}
if "SAMU" in repertoire : 
    print("Samu est bien dans le repertoire")
else : 
    repertoire["SAMU"]= 15
    print(repertoire)