print("---Exercice1---")
def count_digits(text):
    """
    Retourne combien de caractères sont des chiffres (0-9).
    """
    count = 0
    for char in text : 
        if char.isdigit() :
            count += 1 
    return count 

print(count_digits("abc123"))
print(count_digits("no digits!"))

print("---Exercice2---")
def smallest_digit(text):
    """
    Retourne le chiffre le plus petit dans le texte.
    Si aucun chiffre → retourne None.
    """
    smallest = None

    for char in text : 
        if char.isdigit():
            digit = int(char)
            if smallest  is None or digit < smallest :
                smallest = digit

    return smallest
    
print(smallest_digit("a9b2c5"))
print(smallest_digit("hello"))

print("---Exercice3---")
def sum_positive(n):
    """
    Si n < 1 → retourne 0.
    Sinon → somme de 1 à n.
    """
    if n < 1 : 
        return 0
    
    total = 0 
    for number in range(1, n+1) : 
        total += number
    return total

print(sum_positive(1115))

print("---Exercice4---")
def remove_spaces(text):
    """
    Retourne le texte sans aucun espace.
    """
    result = ""
    for char in text : 
        if char!= " ":
            result += char 
    return result

print(remove_spaces("Hello World"))
print(remove_spaces("  a b c  "))

print("---Exercice5---")
def is_palindrome(text):
    """
    Retourne True si text est un palindrome.
    Ignore les majuscules.
    """
    text = text.lower()        
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    return text == reversed_text

print(is_palindrome("Kayak"))   






