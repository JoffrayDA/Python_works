print("---Exerice 1---")
def multiply_by(numbers, factor):
    """
    Retourne une nouvelle liste où chaque élément est multiplié par 'factor'.
    Exemple : ([1,2,3], 3) → [3,6,9]
    """
    new_list = []
    product = 1

    for n in numbers : 
        product = n * factor 
        new_list.append(product)
    return new_list
print(multiply_by([1,2,3,4,100], 10))

print("---Exerice 2---")
def count_min_values(numbers):
    """
    Retourne combien d’éléments sont égaux au plus petit nombre de la liste.
    Exemple : [2,1,3,1,5] → 2
    """
    count = 0 
    smallest = numbers[0]
    
    for n in numbers: 
        if n < smallest :
            smallest = n 

    for n in numbers : 
        if n == smallest: 
            count += 1 
    return count 
print(count_min_values([1,1,1,1,44,3,23,54,84,7,5]))

print("---Exerice 3---")
def remove_negative(numbers):
    """
    Retourne une liste sans les valeurs < 0.
    """ 
    new_list = []
    for n in numbers : 
        if n < 0 : 
            new_list.append(n)
    return new_list
print(remove_negative([1,-1,2,-2,66,-666])) 


print("---Exerice 4---")
def first_greater_than(numbers, n):
    """
    Retourne le premier élément > n.
    Si aucun → None.
    """
    first = 0
    for number in numbers : 
        if number > n :
            first = number
            return first 
    return None 
print(first_greater_than([1,3,4,6,9,11], 8))

print("---Exerice 5---")
def count_value_changes(numbers):
    """
    Compte combien de fois la valeur change d’un élément au suivant.
    Exemple : [1,1,2,2,3,1] → changements: 1→2, 2→3, 3→1 → total = 3
    """
    count = 0
    previous = numbers[0]

    for n in numbers[1:]:
        if n != previous:
            count += 1
        previous = n

    return count
print(count_value_changes([1,1,1,2,3,3,6]))