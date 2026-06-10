print("---Exercice1---")
def min_max_scale(numbers):
    """
    Transforme la liste selon le Min-Max Scaling.
    Ex : [2,4,6] → [0.0, 0.5, 1.0]
    """
    min_val = numbers[0]
    max_val = numbers[0]

    for n in numbers:
        if n < min_val:
            min_val = n
        if n > max_val:
            max_val = n

    result = []
    for n in numbers:
        scaled = (n - min_val) / (max_val - min_val)
        result.append(scaled)

    return result

print("---Exercice2---")
def remove_outliers(numbers):
    """
    Retourne la liste sans les outliers.
    """
    total = 0
    count = 0
    for n in numbers:
        total += n
        count += 1
    mean = total / count

    # 2) Calcul écart moyen absolu - partie corrigée par Chat
    total_dev = 0
    for n in numbers:
        total_dev += abs(n - mean)
    mad = total_dev / count

    # 3) Garder seulement les valeurs dans [mean - mad, mean + mad] - partie corrigée par Chat
    low = mean - mad
    high = mean + mad

    result = []
    for n in numbers:
        if low <= n <= high:
            result.append(n)

    return result

print("---Exercice3---")
def chunk_list(lst, size):
    """
    Exemple :
    chunk_list([1,2,3,4,5], 2)
    → [[1,2], [3,4], [5]]
    """
    result = []
    current = []

    for item in lst:
        current.append(item)
        if len(current) == size:
            result.append(current)
            current = []

    if current:  
        result.append(current)

    return result

print("---Exercice4---")
def find_plateaus(numbers):
    """
    Ex :
    [1,1,2,3,3,3,4,5,5] → [(1,2), (3,3), (5,2)]
    Format : (valeur, longueur)
    """
    result = []
    prev = None
    count = 0

    for n in numbers:
        if n == prev:
            count += 1
        else:
            if count >= 2:
                result.append((prev, count))
            count = 1
        prev = n
        
    if count >= 2:
        result.append((prev, count))

    return result

print("---Exercice5---")
def cumulative_stats(numbers):
    """
    Retourne un tuple de 3 listes :
    (min_cumules, max_cumules, moy_cumulees)
    
    Ex : [3,1,4]
    → ([3,1,1], [3,3,4], [3,2,2.666...])
    """
    min_list = []
    max_list = []
    mean_list = []

    total = 0
    min_val = numbers[0]
    max_val = numbers[0]

    count = 0

    for n in numbers:
        count += 1
        total += n

        if n < min_val:
            min_val = n
        if n > max_val:
            max_val = n

        min_list.append(min_val)
        max_list.append(max_val)
        mean_list.append(total / count)

    return (min_list, max_list, mean_list)
