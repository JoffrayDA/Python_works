print("---Exerice 1---")
def list_sum(numbers):
    """
    Retourne la somme de tous les éléments (sans sum()).
    """
    total = 0 

    for n in numbers : 
        total += n
    return total
print(list_sum([1,2,3,4,5,6,7,8,9,10,11,12,13]))

print("---Exerice 2---")
def list_min(numbers):
    """
    Retourne le plus petit élément de la liste.
    """
    shortest = numbers[0]
    for n in numbers : 
        if shortest > n :
            shortest = n
    return shortest
print(list_min([1,2,3,4,5,6,7,8,9,10,11,12,13]))

print("---Exerice 3---")
def count_greater_than(numbers, n):
    """
    Retourne combien d'éléments sont strictement > n.
    """
    count = 0 
    for c in numbers :
        if c > n : 
            count += 1 
    return count 
print(count_greater_than([1,2,3,4,5,6,7,8,9,10,11,12,13], 5))

print("---Exerice 4---")
def filter_negative(numbers):
    """
    Retourne une liste contenant seulement les valeurs < 0.
    """
    negatives = []
    for n in numbers : 
        if n < 0: 
            negatives.append(n)
    return negatives
print(filter_negative([1,2,-3,4,5,-6,-7,8,9,10,-11,12,-13]))

print("---Exerice 5---")
def find_first_index(numbers, value):
    """
    Retourne l'indice du premier 'value' trouvé dans la liste.
    Si non trouvé → -1.
    """
