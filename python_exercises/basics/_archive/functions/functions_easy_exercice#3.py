print("---Exercice 1---")
# retourne n²
def square(n):       
    product = n * n
    return product
print(square(78))

print("---Exercice 2---")
# retourne n³
def cube(n):
    return n ** 3
print(cube(56))

print("---Exercice 3---")
# True/False
def is_even(n): 
    return n % 2 == 0
print(is_even(4842))

print("---Exercice 4---")
# retourne les 2 derniers chars
def last_two(text):  
        return text[-2:]
print(last_two("hello my friendddds"))

print("---Exercice 5---")
#retourne la somme 
def sum_three(a,b,c): 
    return a + b + c
print(sum_three(15, 456,35))