"""
LOOPS EXERCISES – EASY TO MEDIUM LEVEL (SOLUTIONS)
--------------------------------------------------

This file contains the full solutions for:
- for loops
- while loops
- loops + conditions

Each exercise is solved with clean, readable code.
"""


def count_to(n):
    """
    Prints all numbers from 1 up to n (inclusive).
    Using a simple for loop.
    """
    for number in range(1, n + 1):
        print(number)



def sum_to(n):
    """
    Returns the sum of all integers from 1 to n.
    Must be computed manually using a loop.
    """
    total = 0
    for number in range(1, n + 1):
        total += number
    return total



def count_vowels(text):
    """
    Counts how many vowels appear in the string 'text'.
    Vowels: a, e, i, o, u, y (case insensitive).
    """
    vowels = "aeiouy"
    text = text.lower()
    count = 0

    for letter in text:
        if letter in vowels:
            count += 1

    return count



def countdown(n):
    """
    Prints a countdown from n down to 0 using a while loop.
    Prints "GO!" when finished.
    """
    while n >= 0:
        print(n)
        n -= 1

    print("GO!")


print("=== EXERCISE 1 ===")
count_to(5)

print("\n=== EXERCISE 2 ===")
print(sum_to(5))    # expected: 15
print(sum_to(10))   # expected: 55

print("\n=== EXERCISE 3 ===")
print(count_vowels("hello"))     # expected: 2
print(count_vowels("PYTHON"))    # expected: 1
print(count_vowels("ChatGPT"))   # expected: 1

print("\n=== EXERCISE 4 ===")
countdown(5)
