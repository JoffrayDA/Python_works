# ============================================================
# LISTS.PY — Listes Python
# Python_Works/basics/lists.py
# Coach : Claude | Contexte : e-commerce / Amazon / RH
# ============================================================


# ────────────────────────────────────────────────────────────
# EXERCICE 1 — Manipulation de base
# ────────────────────────────────────────────────────────────
# Tu as une liste de SKUs Amazon.
# 1. Ajoute "DE-009" à la fin
# 2. Insère "FR-000" au début (index 0)
# 3. Supprime "UK-003" de la liste
# 4. Affiche la longueur finale de la liste

skus = ["FR-001", "FR-002", "UK-003", "DE-004", "IT-005"]

# Ton code ici :


# ────────────────────────────────────────────────────────────
# EXERCICE 2 — Slicing
# ────────────────────────────────────────────────────────────
# À partir de la liste `ventes_semaine`, récupère :
#   a) Les 3 premiers jours
#   b) Les 2 derniers jours
#   c) Les jours du milieu (index 2 à 4 inclus)
# Affiche chaque résultat.

ventes_semaine = [120, 95, 140, 200, 180, 160, 90]
# Lundi=120, Mardi=95, Mercredi=140, Jeudi=200,
# Vendredi=180, Samedi=160, Dimanche=90

# a)

# b)

# c)


# ────────────────────────────────────────────────────────────
# EXERCICE 3 — Boucle sur une liste + condition
# ────────────────────────────────────────────────────────────
# Parcours la liste `stocks` et affiche pour chaque produit :
# "⚠️ Stock critique : <nom>" si stock < 15
# "✅ Stock OK : <nom>"       sinon
# Format attendu : utilise des tuples (nom, quantite)

stocks = [
    ("Croquettes 2kg", 8),
    ("Pâtée boeuf", 45),
    ("Friandises chat", 3),
    ("Litière premium", 120),
    ("Jouet souris", 12),
]

# Ton code ici :


# ────────────────────────────────────────────────────────────
# EXERCICE 4 — List comprehension simple
# ────────────────────────────────────────────────────────────
# Tu as une liste de prix HT. Crée une nouvelle liste `prix_ttc`
# avec tous les prix convertis en TTC (× 1.20).
# Fais-le en UNE SEULE LIGNE avec une list comprehension.

prix_ht = [9.99, 24.99, 4.50, 49.99, 14.99]

prix_ttc = []  # remplace [] par ta list comprehension

# print(prix_ttc)
# attendu : [11.988, 29.988, 5.4, 59.988, 17.988]


# ────────────────────────────────────────────────────────────
# EXERCICE 5 — List comprehension avec filtre
# ────────────────────────────────────────────────────────────
# À partir de `commandes`, crée une liste `grosses_commandes`
# qui contient uniquement les montants > 50€.
# Une seule ligne.

commandes = [12.5, 89.0, 45.0, 130.0, 23.5, 67.0, 8.99, 55.0]

grosses_commandes = []  # ta list comprehension ici

# print(grosses_commandes)
# attendu : [89.0, 130.0, 67.0, 55.0]


# ────────────────────────────────────────────────────────────
# EXERCICE 6 — Trier et trouver
# ────────────────────────────────────────────────────────────
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

# 2.

# 3.

# 4.


# ────────────────────────────────────────────────────────────
# EXERCICE 7 — enumerate() et zip()
# ────────────────────────────────────────────────────────────
# Partie A — enumerate()
# Affiche chaque produit avec son numéro de rang (en partant de 1).
# Format : "1. Croquettes 2kg"

produits = ["Croquettes 2kg", "Pâtée boeuf", "Friandises chat", "Litière premium"]

# Ton code avec enumerate() :


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