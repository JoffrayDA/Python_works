print("Exercice1---Le Cri de Guerre")
mots = ["python", "est", "cool"]

for m in mots : 
    print(m.upper(), end=" ")
print("--------------------------")


print("Exercice2---Le Filtre de Chiffres")
scores = [5, 12, 8, 20, 7, 15]
meilleurs_scores = []

for s in scores : 
    if s > 10 : 
        meilleurs_scores.append(s)

print(meilleurs_scores)
print("--------------------------")


print("Exercice3---Le Multiplicateur")
nombres = [1, 2, 3, 4, 5]
nombres_fois_2 = []

for n in nombres : 
    nombres_fois_2.append(n*2)

print(nombres_fois_2)
print("--------------------------")


print("Exercice4---Chercher l'intrus")
donnees = [14, 25, 0, 32, 11]

for i, d in enumerate(donnees) : 
    if d == 0 :
        print(f"J'ai trouvé le zéro à l'index {[i]}.")
print("--------------------------")


print("Exercice5---Accumulateur")
depenses = [10.5, 20, 5, 4.5]
total = 0 

for d in depenses : 
    total += d
print("Total des dépenses :", total)





