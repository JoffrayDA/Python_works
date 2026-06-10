print("-----Exercice1-Extraction de coordonnées")
points = [[48.8, 2.3], [45.7, 4.8], [43.2, 5.3]]
latitudes = []

for p in points : 
    latitudes.append(p[0])
print(latitudes)

print("------------------------")
print("-----Exercice2-Extraction de coordonnées")
scores = [12, 45, 7, 23, 56, 10]
scores.sort(reverse = True)
meilleurs_scores = scores[0:3]
print(meilleurs_scores)


print("------------------------")
print("-----Exercice3-Le Flattening")
groups = [["Alice", "Bob"], ["Charlie"], ["David", "Eve"]]
flat_list = []

for sub_list in groups : 
    for name in sub_list : 
        flat_list.append(name)
print(flat_list)


print("------------------------")
print("-----Exercice4-Exercice de comprehension")
data = [[1, 15.5], [2, 999], [3, 14.2]]
clean_values = []

for ligne in data:
    valeur = ligne[1] 
    
    if valeur != 999:
        clean_values.append(valeur)

print(clean_values) 


print("------------------------")
print("-----Exercice5-Trouver la position")
preds = [0, 0, 1, 0, 1, 1, 0]
indices_un = []
for i in range(len(preds)):
        if preds[i] == 1 : 
             indices_un.append(i)
print(indices_un)