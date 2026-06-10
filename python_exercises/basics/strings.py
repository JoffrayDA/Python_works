# ============================================================
# STRINGS.PY — Chaînes de caractères Python
# Python_Works/basics/strings.py
# Coach : Claude | Contexte : e-commerce / Amazon / RH
# ============================================================


# ────────────────────────────────────────────────────────────
# EXERCICE 1 — Méthodes de base
# ────────────────────────────────────────────────────────────
# À partir de la string `titre`, applique dans l'ordre :
# 1. Affiche en majuscules
# 2. Affiche en minuscules
# 3. Affiche avec la première lettre de chaque mot en majuscule (.title())
# 4. Affiche la longueur (nombre de caractères)
# 5. Vérifie si "bio" est dans la string (True/False) — insensible à la casse

titre = "  croquettes BIO saumon adulte 2kg  "

# 1.

# 2.

# 3.

# 4.

# 5. (pense à .lower() avant de chercher)


# ────────────────────────────────────────────────────────────
# EXERCICE 2 — Nettoyage de données
# ────────────────────────────────────────────────────────────
# En e-commerce, les données arrivent souvent sales.
# Nettoie chaque string selon la consigne.

ref_sale   = "  FR-001 "        # → "FR-001" (strip)
prix_sale  = "24,99€"           # → 24.99 (float propre — remplace , par . et retire €)
marche_sale = "france "         # → "FR" (strip + upper + slice [:2])
asin_sale  = "b08n5wrwnw"       # → "B08N5WRWNW" (ASIN Amazon toujours en majuscules)

# Ton code ici :
# ref_propre    =
# prix_propre   =
# marche_propre =
# asin_propre   =

# print(ref_propre, type(ref_propre))
# print(prix_propre, type(prix_propre))
# print(marche_propre, type(marche_propre))
# print(asin_propre, type(asin_propre))


# ────────────────────────────────────────────────────────────
# EXERCICE 3 — Split et join
# ────────────────────────────────────────────────────────────
# Partie A — split()
# La string `ligne_csv` est une ligne d'export Amazon.
# Sépare-la par ";" et affiche chaque champ sur une ligne.

ligne_csv = "B08N5WRWNW;Croquettes Bio 2kg;24.99;FR;340"

# Ton code :


# Partie B — join()
# Recrée la même string à partir d'une liste de champs
# mais en séparant avec une virgule cette fois.

champs = ["B08N5WRWNW", "Croquettes Bio 2kg", "24.99", "FR", "340"]

# ligne_csv_virgule =
# print(ligne_csv_virgule)
# attendu : "B08N5WRWNW,Croquettes Bio 2kg,24.99,FR,340"


# ────────────────────────────────────────────────────────────
# EXERCICE 4 — f-strings
# ────────────────────────────────────────────────────────────
# Génère des messages formatés avec des f-strings.
# Les valeurs sont données — tu crées juste les strings.

nom_produit = "Croquettes Bio 2kg"
prix        = 24.99
stock       = 340
marche      = "FR"
croissance  = 0.2637  # 26.37%

# 1. Affiche : "Produit : Croquettes Bio 2kg | Prix : 24.99€ | Stock : 340 unités"

# 2. Affiche le taux arrondi à 1 décimale : "Croissance : 26.4%"
#    (utilise :.1f dans la f-string)

# 3. Affiche avec le prix sur 8 caractères aligné à droite :
#    "FR |    24.99€"
#    (utilise :>8.2f)


# ────────────────────────────────────────────────────────────
# EXERCICE 5 — replace() et startswith() / endswith()
# ────────────────────────────────────────────────────────────
# Tu reçois une liste de références produits.
# 1. Filtre et affiche uniquement celles qui commencent par "FR-"
# 2. Remplace tous les tirets par des underscores dans toute la liste
#    (nouvelle liste — pas de modification en place)

references = ["FR-001", "DE-004", "FR-012", "UK-003", "FR-099", "IT-007", "FR-044"]

# 1. (utilise startswith)

# 2. (utilise replace dans une list comprehension)


# ────────────────────────────────────────────────────────────
# EXERCICE 6 — Synthèse : parser une string brute
# ────────────────────────────────────────────────────────────
# Écris une fonction `parser_ref(ref_brute)` qui prend une
# référence produit au format "  fr-001_bio " (mal formatée)
# et retourne un dictionnaire avec :
#   - "marche" : les 2 premières lettres en majuscules ("FR")
#   - "id"     : les 3 derniers chiffres ("001")
#   - "variante": le suffixe après "_" en majuscules ("BIO"),
#                 ou None si pas de "_"
#
# Exemple :
# parser_ref("  fr-001_bio ")  → {"marche": "FR", "id": "001", "variante": "BIO"}
# parser_ref("  de-042 ")      → {"marche": "DE", "id": "042", "variante": None}
#
# Étapes suggérées :
#   1. strip() + lower()
#   2. Sépare sur "_" pour récupérer la variante
#   3. Sépare sur "-" pour récupérer marché et id
#   4. Nettoie et mets en majuscules

def parser_ref(ref_brute):
    pass


# Test
# print(parser_ref("  fr-001_bio "))
# → {"marche": "FR", "id": "001", "variante": "BIO"}
# print(parser_ref("  de-042 "))
# → {"marche": "DE", "id": "042", "variante": None}