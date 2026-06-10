print("---Exercice 1---")
def max_of_two(a, b):
    """
    Retourne le plus grand des deux nombres, sans utiliser max().
    """
    max = a 
    if b > a : 
        max = b
    return max 
print(max_of_two(12,9))

print("---Exercice 2---")
def is_vowel(char):
    """
    Retourne True si char est une voyelle (a e i o u y), min ou maj.
    """
    vowels = "aeiouy"
    char = char.lower()

    for l in char: 
        if l in vowels:
            return True
    return False
    
print(is_vowel("E"))

print("---Exercice 3---")
def count_vowels(text):
    """
    Retourne le nombre total de voyelles (a e i o u y).
    """
    count = 0
    vowels = "aeiouy"
    for l in text : 
        if l in vowels :
            count += 1 
    return count 
print(count_vowels("Hi my best friend"))

print("---Exercice 4---")
def first_space_index(text):
    """
    Retourne l'index du premier espace.
    Si pas d'espace → retourne -1.
    """
    index = 0
    for char in text : 
        if char == " ":
            return index 
        else : 
            index += 1 
    return index 
print(first_space_index("Bien le bonjour")) 

print("---Exercice 5---")
def repeat_char(char, n):
    """
    Retourne une chaîne contenant `char` répété `n` fois.
    Ex : repeat_char("a", 5) → "aaaaa"
    """
    result = ""
    for _ in range(n):
        result += char
    return result
    
print(repeat_char("k", 15))
    




