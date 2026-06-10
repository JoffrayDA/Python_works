print("---Exercice1---")
def add_index(numbers):
    """
    Retourne une liste où chaque élément est augmenté de son index.
    Exemple : [10,10,10] → [10,11,12]
    """
    result = []
    for i, n in enumerate(numbers) : 
        result.append(n+i) 
    return result 
    
print(add_index([10,11,12,13,14,15,16,111]))

print("---Exercice2---")
def count_peaks(numbers):
    """
    Compte combien de fois un nombre est STRICTEMENT
    plus grand que le précédent ET le suivant.
    Exemple : [1,3,1,4,2] → 2
    """
    count = 0
    for i in range(1, len(numbers) - 1):
        if numbers [i] > numbers [ i -1 ] and numbers[i] > numbers [ i + 1 ]:
            count += 1 
    return count 

print(count_peaks([1,2,3,2,5,4,2,8,1]))

print("---Exercice3---")
def remove_duplicates(lst):
    """
    Retourne une liste sans doublons,
    en conservant l'ordre d'apparition.
    Exemple : [1,2,2,3,1] → [1,2,3]
    """
    result = []
    for n in lst : 
        if n not in result : 
            result.append(n)
    return result 
print(remove_duplicates([1,2,3,2,3,2,1,1,7,6]))

print("---Exercice4---")
def first_even_after_odd(numbers):
    """
    Retourne le premier nombre PAIR
    qui suit immédiatement un nombre IMPAIR.
    Si aucun → None.
    Exemple : [2,4,3,6,8] → 6
    """

print("---Exercice5---")
def count_sign_changes(numbers):
    """
    Compte combien de fois le signe change
    entre deux éléments consécutifs.
    Exemple : [1,-2,3,-4] → 3
    """
