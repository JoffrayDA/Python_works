print("---Exercice 1---")
def count_lowercase(text):
    """
    Retourne le nombre de lettres minuscules dans le texte.
    """
    count = 0
    for c in text : 
        if c.islower():
            count += 1 
    return count 

print(count_lowercase("Bien le Bonjour Au MonDe qui m'enToure"))

print("---Exercice 2---")
def remove_consonants(text):
    """
    Retourne le texte en gardant seulement les voyelles (min & maj).
    """
    vowels = "aeiouyAEIOUY"
    return "".join(c for c in text if c in vowels)
    
print(remove_consonants("On laisse nos traces comme une visière trop serrée."))

print("---Exercice 3---")
def last_repeated_char(text):
    """
    Retourne la DERNIÈRE lettre qui apparaît au moins 2 fois.
    Sinon → None.
    """
    seen = set()
    last = None

    for c in text:
        if c in seen:
            last = c
        else:
            seen.add(c)

    return last

print(last_repeated_char("J'aime les croquettes pour chien"))

print("---Exercice 4---")
def only_letters(text):
    """
    Retourne True si le texte contient uniquement des lettres (a-z, A-Z).
    """
    for l in text : 
        if l.isdigit():
            return False 
        
    return True 

print(only_letters("Ressers moi de l'eau2"))

print("---Exercice 5---")
def max_space_sequence(text):
    """
    Retourne le nombre maximal d'espaces consécutifs dans le texte.
    """
    max_count = 0
    current = 0

    for c in text:
        if c == " ":
            current += 1
            if current > max_count:
                max_count = current
        else:
            current = 0

    return max_count

print(max_space_sequence("Faut qu'on se barre à Saint-Domingue."))
