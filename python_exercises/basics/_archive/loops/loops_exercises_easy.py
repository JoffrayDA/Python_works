

# ============================================================
# EXERCISE 1 – Print numbers from 1 to 3
# ============================================================

def print_one_to_three():
    for n in range(1, 4):
        print(n)
    """
    Print:
    1
    2
    3

    Use a for loop.
    """
    



# ============================================================
# EXERCISE 2 – Print each letter of a word
# ============================================================

def print_letters(word):
    for i in word:
        print(i)
    """
    Print each letter of the word, one per line.

    Example:
        print_letters("cat")
        c
        a
        t
    """
    



# ============================================================
# EXERCISE 3 – Print 'Hello' 5 times
# ============================================================

def print_hello_five_times():
    for i in range(5):
        print("Hello")

    """
    Print the word 'Hello' exactly 5 times.
    Use a for loop.
    """
    



# ============================================================
# EXERCISE 4 – Count down from 3 to 1
# ============================================================

def countdown_simple():
    n=3
    while n > 0:
        print(n)
        n= n-1 
    """
    Print:
    3
    2
    1

    Use a while loop.
    """



# ============================================================
# EXERCISE 5 – Print even numbers from 0 to 10
# ============================================================

def print_even_numbers():
    for n in range(0,11,2):
        print(n)
    """
    Print all even numbers between 0 and 10 (included):
    0, 2, 4, 6, 8, 10

    Use a for loop.
    """



# ============================================================
# MANUAL TESTS (optional)
# ============================================================

print("EX 1:")
print_one_to_three()

print("\nEX 2:")
print_letters("dog")

print("\nEX 3:")
print_hello_five_times()

print("\nEX 4:")
countdown_simple()

print("\nEX 5:")
print_even_numbers()
