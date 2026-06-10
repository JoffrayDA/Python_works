print("---Exercice 1---")
def print_1_to_20():
# affiche 1 à 20
    for n in range(1,21):
        print(n)
print(print_1_to_20())

print("---Exercice 2---")
def sum_until(n):
# calcule 1 + 2 + ... + n
    total = 0 
    for n in range(n+1):
        total += n 
    return total 
print(sum_until(12))

print("---Exercice 3---")
def count_down(n):
# affiche n → 0
    for i in range(n, -1, -1):
        print(i)
print(count_down(6))

    