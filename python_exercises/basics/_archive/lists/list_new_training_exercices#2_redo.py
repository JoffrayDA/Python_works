print("---Exercice1---")
def double_values(numbers):
    """
    Retourne une liste où chaque élément est doublé.
    Exemple : [1,2,3] → [2,4,6]
    """
    double_list = []

    for n in numbers : 
        double_list.append(n*2)
    return double_list
print(double_values([23,22,15,9]))

print("---Exercice2---")
def count_even(numbers):
    """
    Retourne combien de nombres dans la liste sont pairs.
    """
    count = 0
    for n in numbers : 
        if n % 2 == 0 : 
            count += 1 
    return count
print(count_even([31, 22, 199, 46, 21]))

print("---Exercice3---")
def word_lengths(words):
    """
    Retourne une nouvelle liste contenant la longueur de chaque mot.
    Exemple : ["hi","world"] → [2,5]
    """
    length_list = []

    for w in words : 
        length_list.append(len(w))
    return length_list  
print(word_lengths(["L'île", "de" ,"France" , "et", "ses", "villages"]))

print("---Exercice4---")
def second_largest(numbers):
    """
    Retourne le 2e plus grand élément de la liste.
    Exemple : [1,5,3,2] → 3
    """
    largest = numbers[0]
    second = numbers[1]

    if second > largest:
        largest, second = second, largest

    for n in numbers[2:]:
        if n > largest:
            second = largest
            largest = n
        elif n > second:
            second = n

    return second
print(second_largest([31, 22, 199, 46, 21]))

print("---Exercice5---")
def is_strictly_increasing(numbers):
    """
    Retourne True si chaque élément est strictement supérieur au précédent.
    """
    previous = numbers[0]

    for n in numbers[1:]:
        if n <= previous:
            return False
        previous = n

    return True
