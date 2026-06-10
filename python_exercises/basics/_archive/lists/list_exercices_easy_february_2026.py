print("-----Exercice1-Nettoyage de capteurs")
temp_raw = [15.2, 16.1, 999, 14.8, -50, 15.5, 16.0]
real_temp = []

for t in temp_raw : 
    if t > -20 and t < 50 :
        real_temp.append(t)
print(real_temp)
print("-------------------------")

print("-----Exercice2-Analyse de prix")
prices = [19.99, 5.50, 10.0, 45.0, 12.75]
moyenne = sum(prices) / len(prices)
print("La moyenne des prix est de :", moyenne)
maximum = prices[0]
for p in prices : 
    if p > maximum : 
        maximum = p
print(maximum)

print("-----Exercice3-Préparation de labels")
scores = [0.88, 0.42, 0.95, 0.30, 0.71]
labels = ["Valid" if s >= 0.5 else "Invalid" for s in scores]
print(labels)


print("-----Exercice4-Dé-doublonnage d'IDs")
user_ids = [102, 304, 102, 405, 304, 506, 102]
unique_ids = []
for u in user_ids : 
    if u not in unique_ids : 
        unique_ids.append(u)
print(unique_ids)


print("-----Exercice5-Dé-doublonnage d'IDs")
images = ["img1", "img2", "img3", "img4", "img5", "img6", "img7", "img8", "img9", "img10"]
batch_size = 3
batches = []

for i in range(0, len(images), batch_size):
    batch = images[i : i + batch_size]
    batches.append(batch)

print(batches)
