print("----Exercice 1----")
def last_char(text) : 
    if text == "":
        return ""
    else :
        return text[-1]
print(last_char("Hello my friend"))

print("----Exercice 2 ----")
def perimeter(length, width):
    return 2*(length+width)
print(perimeter(78,12))

print("----Exercice 3----")
def maximum(a, b, c):
    largest = a 

    if b > largest :
        largest = b

    elif c > largest : 
        largest = c
    
    return largest
print(maximum(165,12,47))

print("----Exercice 4----")
def contains_word_a(text):
    if "a" in text :
        return True
    else : 
        return False
print(contains_word_a("Yalalalaiiiie"))

print("----Exercice 5----")
def count_vowels(text):
    vowels = "aeiouy"
    count = 0

    for char in text.lower():
        if char in vowels :
            count += 1 
    return count 
print(count_vowels("Abalabibabuu"))