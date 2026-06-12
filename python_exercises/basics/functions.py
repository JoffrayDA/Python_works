print("10/06/2026")
print("==========================================")
print("EXERCICE 1 — Fonction simple avec return")
print("==========================================")
# Écris une fonction `prix_ttc(prix_ht)` qui prend un prix HT
# et retourne le prix TTC (TVA 20%).

def prix_ttc(prix_ht):

    prix_avec_taxe = prix_ht * 1.2 
    return prix_avec_taxe

print(prix_ttc(200))
print(prix_ttc(100))   # attendu : 120.0
print(prix_ttc(49.99)) # attendu : 59.988


print("==========================================")
print("EXERCICE 2 — Paramètre par défaut")
print("==========================================")
# Écris une fonction `prix_ttc_flexible(prix_ht, taux=0.20)`
# qui calcule le TTC avec un taux de TVA paramétrable.

def prix_ttc_flexible(prix_ht, taux=0.20):
    prix_avec_taxe = prix_ht *(1 + taux) 

    return prix_avec_taxe

print(prix_ttc_flexible(100))        # 120.0
print(prix_ttc_flexible(100, 0.055)) # 105.5 (TVA réduite UK)


print("==========================================")
print("EXERCICE 3 — Conditions dans une fonction")
print("==========================================")
# Écris une fonction `statut_stock(quantite)` qui retourne :
#   - "Rupture"   si quantite == 0
#   - "Critique"  si quantite <= 10
#   - "Normal"    si quantite <= 100
#   - "Surstock"  si quantite > 100

def statut_stock(quantite):
    if quantite == 0 :
        return "Rupture"
    elif quantite <= 10 : 
        return "Critique"
    elif quantite <= 100 : 
        return "Normal"
    else : 
        return "Surstock"

print(statut_stock(0))   # Rupture
print(statut_stock(5))   # Critique
print(statut_stock(50))  # Normal
print(statut_stock(200)) # Surstock


print("==========================================")
print("EXERCICE 4 — Fonction qui appelle une autre fonction")
print("==========================================")
# Écris une fonction `afficher_prix(prix_ht)` qui :
#   1. Appelle prix_ttc_flexible() pour calculer le TTC
#   2. Retourne une string formatée :
#      "HT: 100€ | TTC: 120.0€"
# (Utilise la f-string)

def prix_ttc_flexible(prix_ht, taux = 0.20):
    return prix_ht * (1 + taux)

def afficher_prix(prix_ht):
    prix_ttc = prix_ttc_flexible(prix_ht)

    return f"HT: {prix_ht}€ | TTC: {prix_ttc}€"

print(afficher_prix(100))   # HT: 100€ | TTC: 120.0€
print(afficher_prix(49.99)) # HT: 49.99€ | TTC: 59.988€




# ────────────────────────────────────────────────────────────
# EXERCICE 5 — Plusieurs valeurs retournées
# ────────────────────────────────────────────────────────────
# Écris une fonction `analyse_ventes(ventes)` qui prend
# une liste de chiffres de ventes journalières,
# et retourne (min, max, moyenne) — dans cet ordre.

def analyse_ventes(ventes):
    mini = min(ventes)
    maxi = max(ventes)
    moyenne = sum(ventes) / len(ventes)

    return mini, maxi, moyenne

mini, maxi, moyenne = analyse_ventes([100, 200, 150, 300, 50])

print(mini, maxi, moyenne)  

# ────────────────────────────────────────────────────────────
# EXERCICE 6 — Docstring + robustesse
# ────────────────────────────────────────────────────────────
# Écris une fonction `taux_conversion(visites, achats)` qui :
#   - Calcule le taux de conversion : achats / visites * 100
#   - Arrondit à 2 décimales (utilise round())
#   - Retourne 0.0 si visites == 0 (éviter division par zéro)
#   - Ajoute une docstring en français sous le `def`
# Exemple : taux_conversion(1000, 35) → 3.5
#           taux_conversion(0, 35)    → 0.0

def taux_conversion(visites, achats):
    """Écris ta docstring ici."""
    pass


# Test
# print(taux_conversion(1000, 35))  # 3.5
# print(taux_conversion(500, 12))   # 2.4
# print(taux_conversion(0, 35))     # 0.0


# ────────────────────────────────────────────────────────────
# EXERCICE 7 — Fonction récapitulative (synthèse)
# ────────────────────────────────────────────────────────────
# Écris une fonction `rapport_produit(nom, prix_ht, stock, ventes_30j)`
# qui retourne un dictionnaire avec les clés suivantes :
#   - "nom"         : le nom du produit
#   - "prix_ttc"    : le prix TTC (appelle prix_ttc_flexible)
#   - "statut"      : le statut du stock (appelle statut_stock)
#   - "ca_estime"   : prix_ht * ventes_30j (chiffre d'affaires estimé HT)
#
# Exemple :
# rapport_produit("Croquettes Bio 2kg", 24.99, 45, 120)
# → {
#     "nom": "Croquettes Bio 2kg",
#     "prix_ttc": 29.988,
#     "statut": "Normal",
#     "ca_estime": 2998.8
#   }

def rapport_produit(nom, prix_ht, stock, ventes_30j):
    pass


# Test
# r = rapport_produit("Croquettes Bio 2kg", 24.99, 45, 120)
# print(r)