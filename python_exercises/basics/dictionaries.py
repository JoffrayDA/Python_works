# ============================================================
# DICTIONARIES.PY — Dictionnaires Python
# Python_Works/basics/dictionaries.py
# Coach : Claude | Contexte : e-commerce / Amazon / RH
# ============================================================


# ────────────────────────────────────────────────────────────
# EXERCICE 1 — Lecture et accès
# ────────────────────────────────────────────────────────────
# À partir du dictionnaire `produit`, affiche :
# 1. Le nom du produit
# 2. Le prix
# 3. La valeur de la clé "stock_fr" (via le dict imbriqué)
# 4. La valeur de la clé "stock_jp" — qui n'existe pas.
#    Utilise .get() avec "Non disponible" comme valeur par défaut.

produit = {
    "nom": "Croquettes Bio 2kg",
    "prix_ht": 24.99,
    "marque": "Edgard & Cooper",
    "stock": {
        "stock_fr": 340,
        "stock_de": 120,
        "stock_uk": 85,
    }
}

# 1.

# 2.

# 3.

# 4.


# ────────────────────────────────────────────────────────────
# EXERCICE 2 — Modifier et enrichir un dictionnaire
# ────────────────────────────────────────────────────────────
# À partir du dict `employe` :
# 1. Change le département de "Ventes" à "E-Commerce"
# 2. Ajoute une clé "anciennete" avec la valeur 3
# 3. Supprime la clé "telephone"
# 4. Affiche le dict final

employe = {
    "nom": "Martin Dupont",
    "poste": "Business Analyst",
    "departement": "Ventes",
    "salaire": 38000,
    "telephone": "06 12 34 56 78"
}

# 1.

# 2.

# 3.

# 4.


# ────────────────────────────────────────────────────────────
# EXERCICE 3 — Boucle sur un dictionnaire
# ────────────────────────────────────────────────────────────
# Parcours le dictionnaire `ventes_par_marche` et affiche
# chaque marché avec ses ventes.
# Format : "FR → 1 250 000 €"
# (Tu peux utiliser f-string avec {:,} pour formater les nombres)

ventes_par_marche = {
    "FR": 1250000,
    "DE": 980000,
    "UK": 1100000,
    "IT": 430000,
    "ES": 390000,
    "NL": 210000,
}

# Ton code ici (utilise .items()) :


# ────────────────────────────────────────────────────────────
# EXERCICE 4 — Dict comprehension
# ────────────────────────────────────────────────────────────
# À partir de `ventes_par_marche` (exercice 3),
# crée un nouveau dict `objectifs` où chaque valeur
# est augmentée de 15% (objectif de croissance).
# Fais-le en UNE SEULE LIGNE avec une dict comprehension.
# Arrondis à l'entier (int() ou round()).

objectifs = {}  # ta dict comprehension ici

# print(objectifs)
# attendu : {"FR": 1437500, "DE": 1127000, ...}


# ────────────────────────────────────────────────────────────
# EXERCICE 5 — Compter avec un dictionnaire
# ────────────────────────────────────────────────────────────
# Tu reçois une liste de départements RH.
# Crée un dictionnaire `compteur` qui compte
# le nombre d'employés par département.
# Utilise .get() pour éviter les KeyError.
#
# Résultat attendu :
# {"Ventes": 3, "Tech": 2, "Marketing": 2, "RH": 1, "Finance": 2}

departements = [
    "Ventes", "Tech", "Marketing", "Ventes",
    "RH", "Tech", "Finance", "Marketing",
    "Ventes", "Finance"
]

compteur = {}

# Ton code ici :


# print(compteur)


# ────────────────────────────────────────────────────────────
# EXERCICE 6 — Liste de dictionnaires
# ────────────────────────────────────────────────────────────
# Tu as un catalogue de produits (liste de dicts).
# 1. Affiche uniquement les noms des produits
# 2. Affiche les produits avec stock > 50
# 3. Calcule le chiffre d'affaires potentiel total
#    (prix_ht * stock pour chaque produit, puis somme)
# 4. Trouve le produit le plus cher (prix_ht max)

catalogue = [
    {"nom": "Croquettes 2kg",    "prix_ht": 24.99, "stock": 340},
    {"nom": "Pâtée boeuf 400g",  "prix_ht": 3.49,  "stock": 820},
    {"nom": "Friandises chat",   "prix_ht": 8.99,  "stock": 45},
    {"nom": "Litière premium",   "prix_ht": 19.99, "stock": 12},
    {"nom": "Brosse poils longs","prix_ht": 14.99, "stock": 67},
]

# 1.

# 2.

# 3.

# 4.


# ────────────────────────────────────────────────────────────
# EXERCICE 7 — Fusionner des dictionnaires
# ────────────────────────────────────────────────────────────
# Tu as les données Amazon de deux trimestres.
# Fusionne-les en un seul dict `annuel`.
# Si un marché apparaît dans les deux, additionne les ventes.
# ⚠️ Ne pas écraser — additionner.
#
# Résultat attendu :
# {"FR": 680000, "DE": 510000, "UK": 590000, "IT": 230000, "NL": 95000}

q1 = {"FR": 320000, "DE": 240000, "UK": 290000}
q2 = {"FR": 360000, "DE": 270000, "UK": 300000, "IT": 230000, "NL": 95000}

annuel = {}

# Ton code ici :


# print(annuel)


# ────────────────────────────────────────────────────────────
# EXERCICE 8 — Synthèse : fonction + dict + logique
# ────────────────────────────────────────────────────────────
# Écris une fonction `analyser_catalogue(catalogue)`
# qui prend une liste de dicts produit (comme exercice 6)
# et retourne un dictionnaire avec :
#   - "nb_produits"   : nombre total de produits
#   - "ca_total_ht"   : somme de (prix_ht * stock) pour tous les produits
#   - "produit_cher"  : nom du produit avec le prix_ht le plus élevé
#   - "en_rupture"    : liste des noms des produits avec stock == 0
#
# Teste avec le catalogue ci-dessous.

def analyser_catalogue(catalogue):
    pass


# Test
catalogue_test = [
    {"nom": "Croquettes 2kg",    "prix_ht": 24.99, "stock": 340},
    {"nom": "Pâtée boeuf 400g",  "prix_ht": 3.49,  "stock": 0},
    {"nom": "Friandises chat",   "prix_ht": 8.99,  "stock": 45},
    {"nom": "Litière premium",   "prix_ht": 19.99, "stock": 0},
    {"nom": "Brosse poils longs","prix_ht": 14.99, "stock": 67},
]

# result = analyser_catalogue(catalogue_test)
# print(result)
# attendu :
# {
#   "nb_produits": 5,
#   "ca_total_ht": arrondi à calculer,
#   "produit_cher": "Croquettes 2kg",
#   "en_rupture": ["Pâtée boeuf 400g", "Litière premium"]
# }