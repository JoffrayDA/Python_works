"""
Exercice : catégorie d'âge

Objectif
--------
S'entraîner à utiliser les conditions if / elif / else.

Règle :
- si l'âge est strictement inférieur à 13  -> "enfant"
- si l'âge est entre 13 et 17 inclus       -> "adolescent"
- si l'âge est supérieur ou égal à 18      -> "adulte"
"""


def age_category(age):

    if age < 13 : 
        print("enfant")
    elif age < 13 and age > 17 : 
        print("adolescent")
    else :
        print("adulte")
    pass


if __name__ == "__main__":
    # Tu peux changer ces valeurs pour tester
    print(age_category(8))   # devrait afficher "enfant"
    print(age_category(15))  # devrait afficher "adolescent"
    print(age_category(21))  # devrait afficher "adulte"
