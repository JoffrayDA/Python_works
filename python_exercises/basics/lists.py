print("12/06/2026")
print("==========================================")
print("EXERCICE 1 — Manipulation de base")
print("==========================================")
# Tu as une liste de SKUs Amazon.
# 1. Ajoute "DE-009" à la fin
# 2. Insère "FR-000" au début (index 0)
# 3. Supprime "UK-003" de la liste
# 4. Affiche la longueur finale de la liste

skus = ["FR-001", "FR-002", "UK-003", "DE-004", "IT-005"]

skus.append("DE-009")
skus.insert(0, "FR-000")
skus.remove("UK-003")
print(len(skus))
print(skus)

print("==========================================")
print("EXERCICE 2 — Slicing")
print("==========================================")
# À partir de la liste `ventes_semaine`, récupère :
#   a) Les 3 premiers jours
#   b) Les 2 derniers jours
#   c) Les jours du milieu (index 2 à 4 inclus)

ventes_semaine = [120, 95, 140, 200, 180, 160, 90]

# a) 
print(f"Les trois premiers jours : {ventes_semaine[:3]}.")
# b)
print(f"Les deux derniers jours : {ventes_semaine[-2:]}.")
# c)
print(f"Les jours du milieu : {ventes_semaine[2:5]}.")


print("==========================================")
print("EXERCICE 3 — Boucle sur une liste + condition")
print("==========================================")
# Parcours la liste `stocks` et affiche pour chaque produit :
# "⚠️ Stock critique : <nom>" si stock < 15
# "✅ Stock OK : <nom>"       sinon

stocks = [
    ("Croquettes 2kg", 8),
    ("Pâtée boeuf", 45),
    ("Friandises chat", 3),
    ("Litière premium", 120),
    ("Jouet souris", 12),
]

# Ton code ici :
for s in stocks : 
    if s[1] < 15 : 
        print(f"⚠️ Stock critique : , {s[0]}.")
    else :
        print(f"✅ Stock OK : , {s[0]}.")

print("==========================================")
print("EXERCICE 4 — List comprehension simple")
print("==========================================")
# Tu as une liste de prix HT. Crée une nouvelle liste `prix_ttc`
# avec tous les prix convertis en TTC (× 1.20).
# Fais-le en UNE SEULE LIGNE avec une list comprehension.

prix_ht = [9.99, 24.99, 4.50, 49.99, 14.99]

prix_ttc = [n * 1.2 for n in prix_ht ] 

print(prix_ttc)       # attendu : [11.988, 29.988, 5.4, 59.988, 17.988]


print("==========================================")
print("EXERCICE 5 — List comprehension avec filtre")
print("==========================================")
# À partir de `commandes`, crée une liste `grosses_commandes`
# qui contient uniquement les montants > 50€.
# Une seule ligne.

commandes = [12.5, 89.0, 45.0, 130.0, 23.5, 67.0, 8.99, 55.0]

grosses_commandes = [c for c in commandes if c > 50]  

print(f"Grosses commandes :{grosses_commandes}.")

print("==========================================")
print("EXERCICE 6 — Trier et trouver")
print("==========================================")

# À partir de `ventes_30j` :
# 1. Affiche la liste triée du + petit au + grand
# 2. Affiche la liste triée du + grand au + petit
# 3. Affiche le top 3 des meilleures ventes (liste)
# 4. Affiche le total des ventes (sum)
#
# ⚠️ N'utilise pas sort() — utilise sorted() pour garder
# la liste originale intacte.

ventes_30j = [320, 150, 480, 95, 600, 210, 380, 440, 75, 510]

# 1.
ventes_croissantes = sorted(ventes_30j)
print(f"Liste ordre croissant : {ventes_croissantes}")
# 2.
ventes_decroissantes = sorted(ventes_30j, reverse = True)
print(f"Liste ordre décroissant : {ventes_decroissantes}.")
# 3.
top_3 = ventes_decroissantes[:3]
print(f"Top 3 des ventes : {top_3}")    
# 4.
print(f"Total des ventes : {sum(ventes_30j)}")

# ────────────────────────────────────────────────────────────
# EXERCICE 7 — enumerate() et zip()
# ────────────────────────────────────────────────────────────
# Partie A — enumerate()
# Affiche chaque produit avec son numéro de rang (en partant de 1).
# Format : "1. Croquettes 2kg"

produits = ["Croquettes 2kg", "Pâtée boeuf", "Friandises chat", "Litière premium"]

for rank, p in enumerate(produits) : 
    print(f"{rank}. {p}")

# Partie B — zip()
# Associe chaque produit à son stock et affiche :
# "Croquettes 2kg → 34 unités"

noms   = ["Croquettes 2kg", "Pâtée boeuf", "Friandises chat"]
stocks_b = [34, 12, 89]

# Ton code avec zip() :


# ────────────────────────────────────────────────────────────
# EXERCICE 8 — Synthèse : fonction + liste + comprehension
# ────────────────────────────────────────────────────────────
# Écris une fonction `top_produits(ventes_liste, seuil)`
# qui prend une liste de tuples (nom, ventes_unites)
# et retourne une liste des noms des produits
# dont les ventes dépassent le seuil.
# Utilise une list comprehension dans la fonction.
#
# Exemple :
# catalogue = [
#     ("Croquettes 2kg", 450),
#     ("Pâtée boeuf", 120),
#     ("Friandises chat", 890),
#     ("Litière premium", 60),
# ]
# top_produits(catalogue, 200) → ["Croquettes 2kg", "Friandises chat"]

def top_produits(ventes_liste, seuil):
    pass


# Test
catalogue = [
    ("Croquettes 2kg", 450),
    ("Pâtée boeuf", 120),
    ("Friandises chat", 890),
    ("Litière premium", 60),
]
# print(top_produits(catalogue, 200))
# attendu : ["Croquettes 2kg", "Friandises chat"]