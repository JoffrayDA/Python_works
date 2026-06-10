weapons = ["sword", "axe", "bow", "dagger", "crossbow"]

#Print each elements in the list
for item in weapons : 
    print(item)

#Print each elements in the list with his index 
for i  in range(len(weapons)) : 
    print(i, "-", weapons[i])

print("-------------------------------")

#Print each elements in the list with his index with enumerate
for i, item in enumerate(weapons): 
    print(i, "-", item)
print("-------------------------------")

#Create a new list with the weapons that have more than 4 caracteres. 
new_long_list_weapons = []
for item in weapons : 
    if len(item)>4 : 
        new_long_list_weapons.append(item)
print(" List of items with more than 4 caracteres : ",new_long_list_weapons)