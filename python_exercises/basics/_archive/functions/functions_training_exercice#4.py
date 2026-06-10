print("---Exercice1---")
def count_non_letters(text):
    """
    Retourne combien de caractères NE sont PAS des lettres.
    (Ex : chiffres, espaces, ponctuation...)
    """
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = 0 

    for c in text : 
        if c in letters : 
            count += 1 
    return count 

print(count_non_letters("Qui sommes nous vraiment ? 145"))

print("---Exercice2---")
def keep_consonants(text):
    """
    Retourne uniquement les consonnes du texte (min & maj).
    """
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"

    return "".join(c for c in text if c in consonants)

print(keep_consonants("Salut aux terriens !"))

print("---Exercice3---")
def first_unique_char(text):
    """
    Retourne le premier caractère qui n'apparaît qu'une seule fois.
    Sinon → None.
    """
    freq = {}

    for c in text : 
        if c in freq : 
            freq[c] += 1 
        else :
            freq[c] = 1
    for c in text : 
        if freq[c] == 1:
            return c 
        return None     
        
print(first_unique_char("I'm the man on the moon"))

print("---Exercice4---")
def contains_digit(text):
    """
    Retourne True si le texte contient au moins un chiffre.
    """
    digits = "0123456789"
    for c in text : 
        if c in digits :
            return True 
        return False

print(contains_digit("I can't feel my face1"))

print("---Exercice5---")
def longest_char_sequence(text):
    """
    Retourne la longueur de la plus longue répétition 
    du même caractère consécutif.
    """
    max_seq = 0
    current = 0
    previous = None 

    for c in text:
        if c == previous:
            current += 1
        else:
            current = 1   
        previous = c

        if current > max_seq:
            max_seq = current

    return max_seq

print(longest_char_sequence("Plus de lllarmes dans le cours, plus de larmes dans la machine"))

