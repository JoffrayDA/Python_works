# ============================================================
# MINI_PROJECTS.PY — Projets récapitulatifs Phase 1
# Python_Works/basics/mini_projects.py
# Coach : Claude | Contexte : e-commerce / Amazon / RH
# ============================================================
# ⚠️ Ces projets sont à faire EN DERNIER, une fois les 5
# autres fichiers complétés et validés.
# Chaque projet mobilise plusieurs compétences à la fois.
# ============================================================


# ════════════════════════════════════════════════════════════
# MINI-PROJET 1 — Tableau de bord Amazon (Vendor)
# ════════════════════════════════════════════════════════════
# Contexte : tu gères le canal Amazon Vendor d'Edgard & Cooper.
# Tu reçois des données brutes sur 6 marchés.
#
# Ta mission :
# 1. Calcule le CA total du canal
# 2. Calcule la part de chaque marché (%) dans le CA total
# 3. Identifie le marché le plus performant
# 4. Affiche un rapport lisible (voir format attendu ci-dessous)
# 5. Identifie les marchés sous la barre des 10% de part de CA
#
# Format de sortie attendu :
# ─────────────────────────────────────────
# TABLEAU DE BORD AMAZON VENDOR — 2024
# ─────────────────────────────────────────
# FR : 3 200 000€  (23.4%)
# DE : 2 800 000€  (20.5%)
# ...
# ─────────────────────────────────────────
# CA Total : 13 700 000€
# Meilleur marché : FR
# Marchés < 10% : ['NL', 'IT']
# ─────────────────────────────────────────

donnees_vendor = {
    "FR": 3_200_000,
    "DE": 2_800_000,
    "UK": 3_100_000,
    "IT": 1_200_000,
    "ES": 1_500_000,
    "NL": 750_000,
    # Note : valeurs fictives pour l'exercice
}

# Ton code ici :


# ════════════════════════════════════════════════════════════
# MINI-PROJET 2 — Analyseur RH
# ════════════════════════════════════════════════════════════
# Contexte : tu analyses la base employés d'une entreprise.
#
# Ta mission :
# 1. Calcule le salaire moyen global
# 2. Calcule le salaire moyen par département
# 3. Liste les employés avec un salaire > moyenne globale
# 4. Compte le nombre d'employés par département
# 5. Identifie le département avec le salaire moyen le plus élevé
#
# Toutes les données sont dans la liste `employes`.
# Écris des fonctions séparées pour chaque étape — pas tout dans le main.

employes = [
    {"nom": "Alice Martin",   "dept": "Tech",       "salaire": 52000},
    {"nom": "Bob Durand",     "dept": "Ventes",     "salaire": 38000},
    {"nom": "Clara Petit",    "dept": "Tech",       "salaire": 48000},
    {"nom": "David Simon",    "dept": "Marketing",  "salaire": 41000},
    {"nom": "Emma Roux",      "dept": "RH",         "salaire": 36000},
    {"nom": "Fabien Morel",   "dept": "Ventes",     "salaire": 42000},
    {"nom": "Gina Leroy",     "dept": "Tech",       "salaire": 61000},
    {"nom": "Hugo Bernard",   "dept": "Marketing",  "salaire": 39000},
    {"nom": "Inès Fontaine",  "dept": "Finance",    "salaire": 55000},
    {"nom": "Jonas Meyer",    "dept": "Finance",    "salaire": 58000},
]

def salaire_moyen(employes):
    pass

def salaire_moyen_par_dept(employes):
    pass

def employes_au_dessus_moyenne(employes):
    pass

def effectif_par_dept(employes):
    pass

def dept_mieux_paye(employes):
    pass

# Appels et affichage :
# moyenne = salaire_moyen(employes)
# print(f"Salaire moyen global : {moyenne}€")
# ...


# ════════════════════════════════════════════════════════════
# MINI-PROJET 3 — Générateur de rapport produit
# ════════════════════════════════════════════════════════════
# Contexte : tu reçois un export CSV brut de produits Amazon.
# Les données sont sales (espaces, majuscules incohérentes,
# prix avec virgule, etc.)
#
# Ta mission :
# 1. Nettoie toutes les données (strip, lower/upper, float)
# 2. Calcule le prix TTC (TVA 20%)
# 3. Détermine le statut stock (Rupture / Critique / Normal / Surstock)
# 4. Calcule le CA potentiel HT (prix_ht * stock)
# 5. Génère un rapport final trié par CA potentiel décroissant
#
# Format de sortie pour chaque produit :
# "Croquettes Bio 2kg | TTC: 29.99€ | Stock: Normal (340) | CA pot.: 8496.6€"

csv_brut = [
    "  croquettes bio 2kg  ; 24,99 ; 340 ",
    "pâtée boeuf 400g;3,49;820",
    "  FRIANDISES CHAT  ; 8,99 ; 0 ",
    "litière PREMIUM;19,99;12",
    "  brosse poils longs ; 14,99 ; 67  ",
    "jouet interactif;  12,50 ;200",
]

# Étapes suggérées :
# 1. Parse chaque ligne (split sur ";", strip chaque champ)
# 2. Crée une liste de dicts nettoyés
# 3. Ajoute les champs calculés
# 4. Trie et affiche

# Ton code ici :