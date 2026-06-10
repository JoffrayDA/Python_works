# ============================================================
# LOOPS.PY — Boucles Python
# Python_Works/basics/loops.py
# Coach : Claude | Contexte : e-commerce / Amazon / RH
# ============================================================


# ────────────────────────────────────────────────────────────
# EXERCICE 1 — for simple sur une liste
# ────────────────────────────────────────────────────────────
# Parcours la liste `marches` et affiche chaque marché
# au format : "Marché actif : FR"

marches = ["FR", "DE", "UK", "IT", "ES", "NL"]

# Ton code ici :


# ────────────────────────────────────────────────────────────
# EXERCICE 2 — for avec range()
# ────────────────────────────────────────────────────────────
# Affiche les 10 premières semaines de l'année avec un compteur.
# Format : "Semaine 1", "Semaine 2", ..., "Semaine 10"
# Utilise range() — pas de liste à créer.

# Ton code ici :


# ────────────────────────────────────────────────────────────
# EXERCICE 3 — while + break
# ────────────────────────────────────────────────────────────
# Un entrepôt démarre avec 500 unités en stock.
# Chaque vente consomme un nombre aléatoire entre 10 et 30 unités.
# Simule les ventes jusqu'à ce que le stock passe sous 50.
# Affiche après chaque vente : "Vente : -X unités | Stock restant : Y"
# Quand le stock < 50, affiche : "⚠️ Seuil critique atteint !"
#
# Utilise : import random + random.randint(10, 30)

import random
random.seed(42)  # fixe le hasard pour que ton résultat soit reproductible

stock = 500

# Ton code ici :


# ────────────────────────────────────────────────────────────
# EXERCICE 4 — continue
# ────────────────────────────────────────────────────────────
# Parcours la liste `commandes`.
# Ignore (avec `continue`) les commandes annulées (valeur None ou 0).
# Pour les autres, affiche : "Commande traitée : 89.0€"
# À la fin, affiche le total des commandes traitées.

commandes = [89.0, None, 45.0, 0, 130.0, None, 23.5, 67.0, 0, 55.0]

total = 0
# Ton code ici :


# print(f"Total traité : {total}€")


# ────────────────────────────────────────────────────────────
# EXERCICE 5 — Boucle imbriquée
# ────────────────────────────────────────────────────────────
# Tu as 3 marchés et 3 catégories de produits.
# Affiche toutes les combinaisons marché × catégorie.
# Format : "FR - Alimentation"
#
# ⚠️ Utilise deux boucles for imbriquées — pas de zip.

marches_b = ["FR", "DE", "UK"]
categories = ["Alimentation", "Accessoires", "Hygiène"]

# Ton code ici :


# ────────────────────────────────────────────────────────────
# EXERCICE 6 — Accumulateur dans une boucle
# ────────────────────────────────────────────────────────────
# À partir de `ventes_hebdo` (liste de listes — une par semaine),
# calcule et affiche :
# 1. Le total de chaque semaine
# 2. Le grand total sur toutes les semaines
# Format : "Semaine 1 : 845 unités"
#          "Total général : XXXX unités"

ventes_hebdo = [
    [120, 95, 140, 200, 180, 60, 50],   # Semaine 1
    [100, 110, 130, 190, 160, 80, 70],  # Semaine 2
    [90,  80, 150, 210, 175, 90, 65],   # Semaine 3
    [130, 120, 145, 220, 195, 70, 55],  # Semaine 4
]

# Ton code ici :


# ────────────────────────────────────────────────────────────
# EXERCICE 7 — Synthèse : boucle + dict + logique
# ────────────────────────────────────────────────────────────
# Tu reçois une liste de transactions avec leur marché d'origine.
# 1. Construis un dictionnaire `ca_par_marche` qui somme
#    le montant de chaque transaction par marché.
# 2. Affiche le marché avec le plus grand CA.
#
# Format d'affichage :
# "FR : 435.5€"
# "DE : 210.0€"
# ...
# "Meilleur marché : FR (435.5€)"

transactions = [
    {"marche": "FR", "montant": 89.0},
    {"marche": "DE", "montant": 45.0},
    {"marche": "FR", "montant": 130.0},
    {"marche": "UK", "montant": 67.0},
    {"marche": "FR", "montant": 216.5},
    {"marche": "DE", "montant": 165.0},
    {"marche": "UK", "montant": 55.0},
    {"marche": "DE", "montant": 0},
]

ca_par_marche = {}

# Ton code ici :