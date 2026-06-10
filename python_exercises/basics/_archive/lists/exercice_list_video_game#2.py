inventory = ["Sword", "Potion", "Shield", "Bow"]

#Add “Axe” at the end.
inventory.append("Axe")
#Insert “Magic Scroll” in the 2nd position.
inventory.insert(1,"Magic Scrool")
#Modify “Potion” to “Mega Potion”.
inventory[2] = "Mega Potion"
#Remove “Bow”.
inventory.remove("Bow")
#Remove the first element using .pop().
inventory.pop(0)
#Sort the list in alphabetical order.
inventory.sort()
#Check if “Shield” is present.
if "shield" in inventory:
    print("Shield is in the inventory.")
else : 
    print("Shield is not in the inventory.")
#Display the total number of items.
print(inventory)
print("------2nd part-------")

weapons = ["Sword", "Axe", "Dagger", "Crossbow", "Hammer"]

#Display all weapons (simple loop).
for weapon in weapons : 
    print(weapon)

#Display the weapon along with its index 
for i in range(len(weapons)):
    print(i, "-", weapons[i])
print("-----------------------")

#Display the weapon along with its index (enumerate).
for i, weapon in enumerate(weapons):
    print(i, "-", weapon)
print("------3rd part-------")

#weapons_with_a → weapons containing “a”
weapons_with_a = [a for a in weapons if "a" in a.lower()]
print("Weapons with the letter 'a': ", weapons_with_a)

#lowercase_weapons → weapons in lowercase
weapons_lower = [w.lower() for w in weapons ]
print("Weapons in lowercase : ", weapons_lower)

#→ long_weapons → weapons with more than 5 letters
long_weapons = [w for w in weapons if len(w)>5]
print("Long weapons : ", long_weapons)
print("------4th part-------")

characters = [
    ["Arthas", "Warrior", 45],
    ["Lyra", "Mage", 30],
    ["Rengar", "Assassin", 52],
    ["Eldor", "Healer", 28],
    ["Brom", "Warrior", 60]
]

#Add a new character
characters.append(["Perceval", "Knight", 87])

#Display only the Warrior
print("----Warriors----")
for c in characters : 
    if c[1] == "Warrior":
        print(c[0], "-", c[1], "-", c[2])

#Display characters with level > 40
print("----characters with level > 40----")
for c in characters : 
    if c[2]>40:
        print(c[0], "-", c[1], "-", c[2])

#Display all characters nicely:
for c in characters : 
    print("Name :", c[0], "| Class :", c[1], "| Level :", c[2])
