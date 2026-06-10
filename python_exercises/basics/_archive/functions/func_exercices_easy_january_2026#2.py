print("Exercice1---Le Multiplicateur Simple")
def doubler(nombre) :
    return nombre * 2 
print(doubler(15))
print("--------------------------")


print("Exercice2---Vérificateur de Majorité")
def est_majeur(age) : 
    if age >= 18 : 
        return True 
    else : 
        return False
print(est_majeur(17))
print("--------------------------")


print("Exercice3---Calculateur de Périmètre")
def perimetre_carre(cote) : 
    return cote * 4
print(perimetre_carre(88))    
print("--------------------------")



print("Exercice4---Concaténateur de Nom")
def formater_nom(prenom, nom):
    return prenom.upper() + nom.upper()
print(formater_nom("Jose", "Mourinho"))
print("--------------------------")



print("Exercice5---Compteur de 'A'")
def compter_a(texte) : 
    count = 0
    for c in texte : 
        if c == 'A' : 
            count += 1 
    return count
print(compter_a("Tegdrtezeftgayhjjhaujahafoiohjnhabvcgffauhabhvgcft".upper()))
print("--------------------------")
