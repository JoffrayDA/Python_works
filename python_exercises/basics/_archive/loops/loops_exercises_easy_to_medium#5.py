print("-----1st exercice------")
def count_lowercase(text):
    """
    Return how many characters in the string are lowercase letters.
    """
    count = 0
    for char in text:
        if char.islower():
            count += 1 
    return count
print(count_lowercase("yo my G"))

print("-----2nd exercice------")
def contains_negative(numbers):
    """
    Return True if the list contains at least ONE negative number.
    Otherwise return False.
    """
    for n in numbers :
        if n < 0 :
            return True 
print(contains_negative([-5, 3, -1, 0, 12]))

print("-----3rd exercice------")
def print_even_until(n):
    """
    Print all EVEN numbers from 1 to n included.
    """
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i)
print_even_until(12)

print("-----4th exercice------")
def compute_average(numbers):
    """
    Return the average of numbers in the list.
    - Do NOT use sum()
    - Do NOT use len()
    You must calculate manually using loops.

    Example:
        [4, 6, 10] -> 6.66...
    """
    total = 0
    count = 0

    for n in numbers:
        total += n
        count += 1   

    return total / count
print(compute_average([4, 6, 10])) 

print("-----5th exercice------")
def print_until_sum_over_50(numbers):
    """
    Print numbers one by one.
    STOP when the running total exceeds 50.
    """
    total = 0

    for n in numbers:
        print(n)
        total += n

        if total > 50:
            print("STOP – total is now", total)
            break
print_until_sum_over_50([10, 5, 20, 30, 100])

print("-----6th exercice------")
def all_letters(text):
    """
    Return True if ALL characters are letters (a–z or A–Z).
    Otherwise return False.
    """
    for char in text : 
        if not char.isalpha():
            return False
    return True
print(all_letters("hello"))      # True
print(all_letters("HelloWorld")) # True
print(all_letters("Hi !"))       # False (space + '!')
print(all_letters("123"))        # False
