print("Exercice1---Le Gestionnaire de Stock")
liste = ["TV", "Ordinateur", "Téléphone", "Machine à laver", "Grille-pain"]

liste.append("Aspirateur")   # ajoute un élément
liste[2]= "Vélo"             # remplace un élément
liste.pop()                  # retire le dernier élément
print("Nombres d'éléments dans la liste :",len(liste))            # affiche le nombre d'éléments
print(liste)
print("--------------------------")


print("Exercice2---Le chercheur de Maximum")
nombres = [12, 45, 2, 89, 34]
max = nombres[0]

for n in nombres : 
    if n > max :
        max = n
print(max)
print("--------------------------")


print("Exercice3---Le Calculateur de Moyenne")
notes = [14, 9, 18, 15, 12]

somme = sum(notes)
print("Somme des notes :", somme)
moyenne = somme/len(notes)
print("Moyenne des notes :", moyenne)
print("--------------------------")


print("Exercice4---Le Filtre de Prénoms")
names = ["Jean", "Anne", "Maxime", "Léa", "Benoît"]
petits_prenoms = []

for n in names : 
    if len(n) < 5 :
        petits_prenoms.append(n)
print("Liste des prénoms de moins de 5 lettres : ", petits_prenoms)
print("--------------------------")


print("Exercice5---L'Inverseur Manuel")
ma_liste = [1, 2, 3, 4, 5]
new_liste = ma_liste[::-1]

print(new_liste)



