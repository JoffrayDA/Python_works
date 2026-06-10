print("----Exercice 1----")
def word_count(text):
    """
    Retourne un dictionnaire qui compte les occurrences de chaque mot.
    """
    words = text.split()
    freq = {}

    for w in words : 
        if w in freq : 
            freq[w] += 1
        else : 
            freq[w] = 1 
    return freq 

print(word_count("Hello Hello my my friend friend friend"))

print("----Exercice 1- Remake----")
def word_count(text):
    words = text.split()
    freq = {}

    for w in words : 
        if w in freq :
            freq[w] += 1
        else : 
            freq[w] = 1
    return freq

print(word_count("Hello Hello my friend friend friend"))

print("----Exercice 2----")
def invert_dict(d):
    """
    Inverse clés et valeurs.
    """
    inverted = {}
    for key, value in d.items() :
        inverted [value] = key 
    return inverted 
print(invert_dict({"a" : 1, "b" : 2, "c" : 3}))

print("----Exercice 3----")
students = {
    "Pierre": 15,
    "Lucie": 12,
    "Marc": 8,
    "Sarah": 17
}

def get_best_student(students):
    """
    Retourne le prénom de l'étudiant avec la meilleure note.
    """     
    best_name = None
    best_note = -1

    for name, note in students.items() :
        if note > best_note :
            best_note = note 
            best_name = name
    return best_name, best_note

print(get_best_student(students))
