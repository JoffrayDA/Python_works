print("Exercice1---Le Compteur de Fruits")
bulletins = ["Bleu", "Rouge", "Bleu", "Bleu", "Rouge", "Vert"]
resultats = {}

for c in bulletins : 
    if c in resultats : 
        resultats[c] += 1
    else : 
        resultats[c] = 1 
print(resultats)
print("--------------------------")


print("Exercice2---Gestionnaire d'Élèves")
villes_temp = {"Paris": 15, "Nice": 25, "Lille": 8, "Lyon": 12}

for v, t in villes_temp.items() : 
    if t < 10 : 
        print(f"Il fait froid à {v}, seulement {t} degrés !")
("--------------------------")


print("Exercice3---Le Calculateur de Salaire")
travail = {"Lundi": 7, "Mardi": 8, "Mercredi": 5}
tarif = 15
salaire_total = 0 

for h in travail.values() : 
    salaire_total += h * tarif
print(salaire_total)
