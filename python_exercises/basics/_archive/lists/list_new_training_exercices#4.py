print("---Exerice 1---")
def square_at_odd_index(numbers):
    """
    Retourne une liste contenant le carré des éléments
    situés aux index impairs (1, 3, 5, ...).
    Exemple : [2,3,4,5] → [9,25]
    """
    index = 0
    lst_square = []
    
    for n in numbers : 
        if index % 2 != 0:
            lst_square.append(n*n)
        index += 1
    
    return lst_square
print(square_at_odd_index([1, 2, 4, 10, 100, 1000]))

print("---Exerice 2---")
def count_long_words(words, n):
    """
    Retourne combien de mots ont une longueur STRICTEMENT
    supérieure à n.
    Exemple : (["chat","éléphant","chien"], 4) → 1
    """
    count = 0 

    for word in words : 
        if len(word) > n : 
            count += 1 
    return count 
    
print(count_long_words(["chat","éléphant","chien","nuage", "saperlipopette"], 5))

print("---Exerice 3---")
def first_decrease(numbers):
    """
    Retourne l'indice du premier élément qui est
    plus petit que l'élément précédent.
    Si jamais la liste ne décroît pas → retourne -1.
    Exemple : [1,3,5,4,6] → 3
    """
    index = 0 
    first = 0
    previous = -1

print("---Exerice 4---")
def unique_elements(lst):
    """
    Retourne une nouvelle liste contenant chaque élément
    UNE SEULE FOIS, dans l'ordre d'apparition.
    Exemple : [1,2,2,3,1] → [1,2,3]
    """
    seen = set()
    new_lst = []

    for n in lst : 
        if n not in seen :
            new_lst.append(n)
            seen.add(n)
    return new_lst

print(unique_elements([1,2,2,3,4,4,5,6,6,6,11,18,12]))

print("---Exerice 5---")
def sum_between(numbers, a, b):
    """
    Retourne la somme des nombres STRICTEMENT compris
    entre a et b.
    Exemple : ([1,5,3,10,7], 3, 8) → 12  (5 + 7)
    """
    total = 0

    for n in numbers : 
        if n > a and n < b : 
            total += n
    return total
print(sum_between([1,11,22,33], 5, 23))

