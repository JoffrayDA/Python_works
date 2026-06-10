print("---Exercice 1---")
# Crée un dictionnaire "product"
# avec : name, price, category
# puis affiche le prix

product = {
    "name" : "Iphone 12",
    "price" : 1200,
    "category" : "phone"
}

print(product["price"])

print("---Exercice2---")
# Parcours le dictionnaire product
# et affiche :
# name -> valeur

for k, value in product.items() : 
    print(k, "->",  value)


print("---Exercice3---")
scores = ["A", "B", "A", "C", "B", "A"]

# Crée un dictionnaire qui compte
# combien de fois chaque lettre apparaît

count = {}

for s in scores : 
    if s in count : 
        count[s] += 1 
    else : 
        count[s] = 1

print(count)



