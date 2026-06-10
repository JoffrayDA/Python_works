print("---Exerice 1---")
def reverse_list(lst):
    """
    Retourne une nouvelle liste avec les éléments à l'envers.
    Sans reversed() et sans lst[::-1].
    """
    reversed_list = []
    for item in lst : 
        reversed_list = [item] + reversed_list
    return reversed_list

print(reverse_list([1,2,3,4,5,6,7,8,9,19]))

print("---Exerice 2---")
def list_average(numbers):
    """
    Retourne la moyenne des éléments de la liste.
    """
    total = 0
    count = 0
    
    for n in numbers : 
        total += n
        count += 1
    if count == 0 : 
        return None 
    return total / count

print(list_average([1,2,3,4,5,6,7,8,9,19]))

print("---Exerice 3---")
def squares(numbers):
    """
    Retourne une liste contenant le carré de chaque nombre.
    """
    result = []
    for n in numbers : 
        result.append(n*n)
    return result
    
print(squares([1,2,3,4,5,6,7,8,9,19]))

print("---Exerice 4---")
def cumulative_sum(numbers):
    """
    Retourne une liste où chaque élément est la somme cumulée.
    """
    result = []
    total = 0

    for n in numbers : 
        total += n
        result.append(total)
    return result

print(cumulative_sum([1,2,3,4,5,6,7,8,9,19]))


print("---Exerice 5---")
def find_all_indices(lst, value):
    """
    Retourne une liste d'indices où value apparaît.
    """
    indice_lst = []
    index = 0

    for item in lst:
        if item == value:
            indice_lst.append(index)
        index += 1

    return indice_lst
print(find_all_indices([1,2,3,4,5,6,7,8,9,19], 19))









