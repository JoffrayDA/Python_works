print("---Exerice 1---")
def reverse_string(text):
    """
    Retourne le texte inversé sans utiliser text[::-1].
    """
    result = ""
    for c in text:
        result = c + result   
    return result

print(reverse_string("Bonjour"))

print("---Exerice 2---")
def count_words(text):
    """
    Retourne le nombre de mots dans le texte sans utiliser split().
    Un mot = suite de lettres.
    """
    count = 0
    in_word = False

    for c in text:
        if c.isalpha():
            if not in_word:
                count += 1
                in_word = True
        else:
            in_word = False

    return count

print("---Exerice 3---")
def count_alpha(text):
    """
    Retourne le nombre de lettres (a-z, A-Z).
    """
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = 0

    for c in text:
        if c in letters:
            count += 1
    return count

print("---Exerice 4---")
def is_isogram(word):
    """
    Retourne True si aucune lettre n'est répétée.
    Ignore la casse.c
    """
    seen = set()
    for c in word.lower():
        if c in seen:
            return False
        seen.add(c)
    return True

print("---Exerice 5---")
def most_frequent_letter(text):
    """
    Retourne la lettre la plus fréquente dans le texte.
    Ignore majuscules / minuscules.
    Ignore les caractères non alphabétiques.
    """
    text = text.lower()
    letters = "abcdefghijklmnopqrstuvwxyz"
    best_letter = None
    best_count = 0

    for l in letters:
        count = 0
        for c in text:
            if c == l:
                count += 1
        if count > best_count:
            best_count = count
            best_letter = l

    return best_letter

