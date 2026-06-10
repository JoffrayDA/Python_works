print("----Exercice 1----")
def list_sum(numbers):      # somme des éléments
    total = 0
    for n in numbers : 
        total += n
    return total

print(list_sum([1, 2, 3, 4, 7, 34, 12]))  

print("----Exercice 2----")
def list_product(numbers):  # produit
    total = 1
    for n in numbers : 
        total *= n
    return total

print(list_product([1, 2, 3, 4, 7, 34, 12]))

print("----Exercice 3----")
def count_negatives(numbers):   # compte les < 0
    count = 0 
    for n in numbers : 
        if n < 0 :
            count += 1
    return count 

print(count_negatives([1, -2, 3, 4, -7, 34, -12]))

print("----Exercice 4----")
def max_number(numbers):    # sans max()
    largest = numbers [0]
    for n in numbers : 
        if n > largest :
            largest = n
    return largest

print(max_number([1, -2, 3, 4, -7, 34, -12]))

print("----Exercice 5----")
def reverse_list(numbers):  # sans reversed()
    reverse_numbers = []
    for n in numbers : 
        reverse_numbers.insert(0, n)
    return reverse_numbers

print(reverse_list([1, -2, 3, 4, -7, 34, -12]))
    
