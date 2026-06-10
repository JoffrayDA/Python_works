print("Exercice1---Le Menu du Resto")
mot = "banane"
compteur = {}

for c in mot : 
    if c in compteur : 
        compteur[c] += 1 
    else : 
        compteur[c] = 1

print(compteur)
print("--------------------------")


print("Exercice2---Gestionnaire d'Élèves")
classe = { "eleve1": {"nom": "Léo", "note": 15}, "eleve2": {"nom": "Eva", "note": 8} }


for e in classe:
    eleve = classe[e]              
    if eleve["note"] < 10:
        print(f"{eleve['nom']} doit travailler plus.")
print("--------------------------")


print("Exercice3---Le Panier Total")
prix = {"pomme": 2, "lait": 1.5, "pain": 1}
panier = {"pomme": 3, "pain": 2}

prix_panier = 0

for produit, quantite in panier.items():
    prix_panier += prix[produit] * quantite

print(prix_panier)