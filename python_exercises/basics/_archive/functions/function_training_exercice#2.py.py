print("---Exercice 1---")
def count_uppercase(text):
    """
    Retourne le nombre de lettres majuscules dans le texte.
    """
    count = 0 
    for u in text : 
        if u.isupper():
            count += 1 
    return count 

print(count_uppercase("Hello My Dude"))

print("---Exercice 2---")
def remove_vowels(text):
    """
    Retourne le texte sans a, e, i, o, u, y (min & maj).
    """
    vowels = "aeiouyAEIOUY"
    return "".join(c for c in text if c not in vowels)

print(remove_vowels("Hello, it's sunny outside."))

print("---Exercice 3---")
def first_repeated_char(text):
    """
    Retourne la première lettre qui apparaît AU MOINS 2 fois.
    Sinon → None.
    """
    first = set()

    for c in text : 
        if c in first : 
            return c 
        first.add(c)
    return None 

print(first_repeated_char("abca")) 

print("---Exercice 4---")
def all_unique(text):
    """
    Retourne True si chaque caractère apparaît 1 seule fois.
    """
    seen = set()
    
    for c in text:
        if c in seen:  
            return False
        seen.add(c)
    
    return True  

print(all_unique("abc"))    
print(all_unique("hello"))  

print("---Exercice 5---")
def count_words(text):
    """
    Retourne le nombre de mots dans le texte.
    Un mot = suite de lettres sans espace.
    """
    count = 0
    in_word = False
    
    for c in text:
        if c != " " and not in_word:
            count += 1
            in_word = True
        elif c == " ":
            in_word = False
            
    return count

print(count_words("Bien le bonjour mon pote "))
