weapons = ["Sword", "Axe", "Bow", "Dagger", "Crossbow", "Hammer"]

#Create a new list with 4 weapons 
inventory = ["Bow", "bludgeon", "Knife", "brass knuckles"]  

#Add a weapon
inventory.append("Axe")

#Insert a weapon in the second position
inventory.insert(1,"Spear")

#Modify an element of the list
inventory[4] = "Tonfa"

#Delete a weapon
inventory.remove("Bow")

#Delete a weapon with pop
inventory.pop(3)

#Sort the list 
inventory.sort()

#Look if "Bow" is in the list 
if "Bow" in inventory : 
    print("Bow is in the list.")

#Print the lenght of the list 
print(len(inventory))
print("-----------------------------")

#------------------------------------------------------------
#Print every weapons of the weapons list 
for i in weapons : 
    print(i)
print("-----------------------------")

#Print every weapons of the weapons list with his index 
for i in range(len(weapons)):
    print(i, "-",weapons[i])
print("-----------------------------")

#Print every weapons + index with enumerate
for i, weapon in enumerate(weapons):
    print(i, "-",weapon)

#-------------------------------------------------------------
#Create a new list with the weapon with the letter 'a'
weapons_with_a = [w for w in weapons if "a" in w.lower()]
print("Weapons with the letter a :", weapons_with_a)



