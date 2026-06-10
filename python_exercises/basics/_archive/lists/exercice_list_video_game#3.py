inventory = ["Sword", "Herb", "Torch", "Dagger"]

#Replace "Torch" with "Magic Lantern".
inventory[2] = "Magic Lantern"

#Add "Iron Helmet" at the beginning of the list.
inventory.insert(0,"Iron Helmet")

#Add "Gold Coin" 3 times (repetition).
for i in range(3):
    inventory.append("Gold Coin")

#Remove only the first occurrence of "Gold Coin".
inventory.remove("Gold Coin")

#Insert "Mana Potion" in the last position before sorting.
inventory.append("Mana Potion")

#Sort the list in reverse order (Z → A).
inventory.sort(reverse=True)    

#Count how many times "Gold Coin" appears.
gold_coins = inventory.count("Gold Coin")
print("Gold coins appears :",gold_coins)

#Display the first 3 items in your inventory.
print("First three items in the inventory :",inventory[:3])
print("-----2nd part-----")

spells = ["Fireball", "Ice Spike", "Heal", "Lightning Bolt", "Wind Cutter"]

#Display all the spells in Uppercase
for s in spells:
    print(s.upper())    
print("----------------")

#Display the index + the spell à partir de 1
for i, spell in enumerate(spells, start = 1):
    print(i, "-", spell)
print("----------------")

#Display every spells + ("ultimate") if is lenght is more than 10
for i, spell in enumerate(spells, start=1):
    if len(spell) > 10:
        print(i, "-", spell, "(Ultimate)")
    else:
        print(i, "-", spell)
print("----------------")

#Display a Spellbook :
print("--- SPELLBOOK ---")
for spell in spells : 
    print("*", spell)
print("-----3rd part-----")

#Display spells with more than 8 letters
long_spells = []
for spell in spells:
    if len(spell)>8:
        long_spells.append(spell)
print("Spells that have more that 8 letters : ",long_spells)
print("-----------------------")

#Display spells with less than 5 letters
short_spells = []
for spell in spells:
    if len(spell)<5:
        short_spells.append(spell)
print("Spells that have less that 5 letters : ",short_spells)
print("-----------------------")

#Display spells that are wrote in lowercase
lower_spells = []
for spell in spells: 
    if spell.islower():
        lower_spells.append(spell)
print("Spells that are wrote in lowercase : ",lower_spells)
print("-----------------------")     

#Display a list that show the lenght of every spell
spell_lengths = []
for i, spell in enumerate(spells) :
    print(spell,"-",len(spell))
print("-----------------------")     

#Display the spells with the letter "i" in it 
spell_with_i=[s for s in spells if "i" in s]
print(spell_with_i)
print("-----4th part-----")

guild = [
    ["Arthur", "King", 79],
    ["Seren", "Priest", 33],
    ["Kael", "Mage", 58],
    ["Thorne", "Rogue", 41],
    ["Liora", "Archer", 27],
    ["Perceval", "Knight", 82],
    ["Lancelot", "Knight", 86]
]

#Add a new member : ["Draven", "Necromancer", 62]
guild.append(["Draven", "Necromancer", 62])
print("-----------------------")     

#Displays only characters whose class contains an R 
r_members = [m for m in guild if "K" in m[1]]
print("Members who have a 'R' in their class :",r_members)
print("-----------------------")     

#Display members who have a level between 30 and 60
average_level_members = [m for m in guild if 30 <= m[2] <= 60]
print("Members who have a level between 30 and 60 :",average_level_members)
print("-----------------------")     

#Display members who have a level more than 60
elite_members = [m for m in guild if m[2] > 60]
print("Members who have a level of more than 60 :",elite_members)
print("-----5th part-----")

quests = [
    ["Slay the Dragon", "urgent"],
    ["Gather Herbs", "low"],
    ["Protect the Village", "medium"],
    ["Rescue the Prince", "urgent"],
    ["Explore the Ruins", "medium"]
]

#Sort the quests by priority
priority_quests = {"urgent": 1, "medium": 2, "low": 3}
quests.sort(key=lambda q: priority_quests[q[1]])
print("Quests list and priority",quests)
print("-----------------------")     

#Displays quests neatly sorted:
for quest in quests : 
    print(f"[{quest[1].upper()}] {quest[0]}")


