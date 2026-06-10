print("Exercice1---Le Compteur de 'e'")
mots = ["pomme", "banane", "orange", "kiwi"]
compteur = 0 

for m in mots : 
    if "e" in m :
        compteur += 1 
print(compteur)
print("--------------------------")


print("Exercice2---Inverser les signes")
nombres = [10, -5, 12, -3, 8]
new_liste = []

for n in nombres : 
        new_liste.append(n*-1)
print(new_liste)
print("--------------------------")


print("Exercice3---Le chercheur de doublons simple")
nombres = [1, 2, 3, 4, 2, 5]
vus = []

for n in nombres : 
    if n in vus :
        print(f"{n} est un doublon !")
    else : 
        vus.append(n)
print(vus)
print("--------------------------")


print("Exercice4---Concaténation de listes")
prenoms = ["Jean", "Marc"]
noms = ["Dupont", "Durand"]
concat = []

for i in range(len(prenoms)):
    nom_complet = prenoms[i] + " " + noms[i]
    concat.append(nom_complet)

print(concat)
print("--------------------------")


print("Exercice5---Le Mini-Max sans fonction")
notes = [12, 15, 8, 19, 11]
max = notes[0]

for n in notes : 
    if n > max : 
        max = n
print(max)
