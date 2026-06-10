print("Exercice1---Le Mini-Max sans fonction")
cave = ["Bordeaux", "Merlot", "Chablis", "Syrah"]
choix = input("Quel vin cherchez-vous ? ")

if choix in cave : 
    print(f"Oui, nous avons du {choix} en stock !")
else : 
    print(f"Désolé, nous n'avons pas de {choix}.")
print("--------------------------")


print("Exercice2---Le Tri de la Boîte de Nuit")
ages = [14, 22, 17, 45, 12, 30, 18]
majeurs = []
mineurs = []

for a in ages : 
    if a >= 18 : 
        majeurs.append(a)
    else : 
        mineurs.append(a)

print("Majeurs :",majeurs, "Mineurs :", mineurs)
print("--------------------------")


print("Exercice3---Le Comptable Précis")
prix_ht = [10.0, 25.50, 100.0, 49.99]
prix_ttc = []

for p in prix_ht : 
    calcul = round(p * 1.2, 2)
    prix_ttc.append(calcul)
print(prix_ttc)