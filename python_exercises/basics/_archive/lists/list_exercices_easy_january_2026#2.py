print("Exercice1---Le Nettoyeur de Doublons")
nombres = [1, 2, 2, 3, 4, 4, 5, 1]
new_liste = []

for n in nombres : 
    if n not in new_liste : 
        new_liste.append(n)

print(new_liste)
print("--------------------------")


print("Exercice2---Séparateur Pair / Impair")
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pairs = []
impairs = []

for n in nombres : 
    if n % 2 == 0 : 
        pairs.append(n)
    else : 
        impairs.append(n)

print("Liste nombres pairs :", pairs)
print("Liste nombres impairs :",impairs)
print("--------------------------")


print("Exercice3---Le Chercheur d'Indice")
fruits = ["pomme", "banane", "cerise", "orange"]
new_fruit = input("Tape le nom d'un fruit :")


if new_fruit in fruits :
    print(fruits.index(new_fruit))
else : 
    print("Ce fruit n'est pas dans le panier.")
print("--------------------------")


print("Exercice4---Transformateur de Longueurs")
mots = ["Python", "Code", "Liste", "Programmation"]
longueur_mots = []

for c in mots :
    longueur_mots.append(len(c))

print(len(longueur_mots))
print("--------------------------")


print("Exercice5---Le Remplaçant de Négatifs")
temp = [12, -3, 5, -1, 0, 18]

for i, t in enumerate(temp):
    if t < 0:
        temp[i] = 0

print(temp)


