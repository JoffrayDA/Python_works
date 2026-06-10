print("Exercice1---La Machine à Saluer")
def dire_bonjour(nom):
    return f"Yo {nom}"
print(dire_bonjour("Maxwell le brave"))
print("--------------------------")

print("Exercice2---Le Convertisseur de Minutes")
def convertir(minutes) : 
    return minutes * 60
print(convertir(450))
print("--------------------------")


print("Exercice3---Le Calculateur de TTC")
def prix_final(prix_ht, tva) : 
    return prix_ht * tva
print(prix_final(500,1.20))
print("--------------------------")


print("Exercice4---Le Plus Grand des Deux")
def maximum(a, b): 
    if a > b :
        return a 
    else : 
        return b
print(maximum(15454568, 8754451))
print("--------------------------")


print("Exercice5---L'Analyseur de Liste")
def calculer_moyenne(liste_nombres) : 
    count = 0
    for n in liste_nombres : 
        count += n 
    moyenne = count / len(liste_nombres)
    return moyenne
print(round(calculer_moyenne([45,87,54,5454,421,54,1,421,2156,54,5,54854,51,521,54,11,21,1,4564,554,4,4]),2))
print("--------------------------")
