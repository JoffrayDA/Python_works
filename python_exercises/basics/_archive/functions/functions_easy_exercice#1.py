print("----Exercice 1----")
def last_char(text):
    if text == "":
        return ""
    else : return text[-1]
print(last_char("Holidays"))
print(last_char(" "))

print("----Exercice 2 ----")
def perimeter(length, width):
    return 2 * (length + width)
print(perimeter(7,15))

print("----Exercice 3----")
def maximum(a, b, c):
    largest = a 

    if b > largest :
        largest = b
    
    elif c > largest :
        largest = c

    return largest
print(maximum(154, 457, 23))

print("----Exercice 4----")
def contains_a(word):
    if "a" in word :
        return True 
    else : 
        return False
print(contains_a("hyhya"))

print("----Exercice 5----")
def count_vowels(text):
    count = 0
    vowels = "aeiouy"
    for char in text.lower():
        if char in vowels:
            count += 1 
    return count
print(count_vowels("Ablablublibloblu"))



