courses = ["pommes", "bananes", "oeufs"]
courses.append("lait")
courses.remove("bananes")
courses.insert(1,"pâtes")
print(courses)
print(len(courses))

for aliment in courses : 
    print("J'ai besoin de :", aliment)

for i in range(len(courses)):
    print( i + 1, ("-"), courses[i])

####################################################

equipement = []
while True:
    item = input("Ajoute un équipement (ou 'stop' pour finir) : ")
    if item.lower() == "stop":
        break
    equipement.append(item)

print("\nTon équipement complet :", equipement)