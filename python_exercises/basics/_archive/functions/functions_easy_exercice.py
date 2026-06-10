#Write a function that returns the square of a number.
print("----Exercice 1----")
def square(n):
    return n * n
print(square(9))

#Returns a sentence in the style of: "Hello Pierre".
print("----Exercice 2----")
def greet(name):
    return f"Hello {name}"
print(greet("Alain"))

#Returns the average of 3 numbers.
print("----Exercice 3----")
def average(a, b, c):
    return (a + b + c) / 3
print(average(4, 10, 16))  

#Returns True if n is even, otherwise False.
print("----Exercice 4----")
def even(n):
    if n % 2 == 0 :
        return True
    else : 
        return False 
print(even(4))


#Returns the text repeated N times (no use of "text" * N at the moment).
print("----Exercice 5----")
def repeat(text, n):
    result = ""
    for _ in range(n):
        result += text
    return result
print(repeat("Hi", 3))




