print("---Exercice1---")
def elements_at_even_index(lst):
    """
    Retourne une liste contenant les éléments situés aux index pairs (0,2,4,...).
    """
    even_lst = []
    index = 0 

    for n in lst :
        if index % 2 == 0:
            even_lst.append(n)
        index += 1 

    return even_lst
print(elements_at_even_index([22,11,8,9,1,2,4,24,14]))

print("---Exercice2---")
def count_below_average(numbers):
    """
    Calcule la moyenne puis compte les nombres strictement en dessous.
    """
    total = 0
    for n in numbers: 
        total =+ n

    moyenne = total/len(numbers)

    count = 0
    for n in numbers : 
        if n < moyenne : 
            count += 1
    return count
print(count_below_average([121,13,92,74,93,76]))

print("---Exercice3---")
def join_with_hyphen(words):
    """
    Concatène les mots avec '-' entre eux.
    Exemple : ["hello","world"] → "hello-world"
    """
    return "-".join(words)
print(join_with_hyphen(["Hello", "mon", "amour"]))

print("---Exercice4---")
def has_duplicate(lst):
    """
    Retourne True si un élément apparaît au moins deux fois.
    Sinon False.
    """
    seen = set()
    for item in lst : 
        if item in seen : 
            return True 
        seen.add(item)
    return False 
print(has_duplicate("bien le bonjour, vous êtes bien aimable"))

print("---Exercice5---")
def max_gap(numbers):
    """
    Retourne la plus grande différence absolue entre deux éléments consécutifs.
    Exemple : [1,5,2,10] → gaps = [4,3,8] → retourne 8
    """
    max_diff = 0

    for i in range(len(numbers) - 1):
        diff = abs(numbers[i+1] - numbers[i])
        if diff > max_diff:
            max_diff = diff

    return max_diff
print(max_gap([1, 100]))

