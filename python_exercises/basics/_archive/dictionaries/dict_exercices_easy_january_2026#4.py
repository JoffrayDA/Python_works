print("Exercice1---Le Compteur de Fruits")
panier = ["pomme", "banane", "pomme", "orange", "banane", "pomme"]
inventaire = {}

for f in panier : 
    if f in inventaire :
        inventaire[f] += 1 
    else : 
        inventaire[f] = 1 
print(inventaire)
print("--------------------------")


print("Exercice2---Gestionnaire d'Élèves")
magasin = {"DVD": 20, "Consoles": 2, "Jeux": 15, "Manettes": 3}

for i, q in magasin.items(): 
    if q < 5 : 
        print(f"Alerte ! Il ne reste que {q} {i}")
print("--------------------------")


print("Exercice3---La Note Finale")
epreuves = {"Maths": 15, "Sport": 10, "Anglais": 14}
coeff = 2
total_points = 0 

for note in epreuves.values():
    total_points += (note * coeff)

print(f"Le total des points est de : {total_points}")
