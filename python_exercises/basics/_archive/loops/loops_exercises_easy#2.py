# ============================================================
# EXERCISE 1 – Print numbers from 10 down to 6
# ============================================================

def print_ten_to_six():
    n=0
    for n in range(10,5,-1):
        print(n)
        n= n-1
    """
    Print the numbers:
    10
    9
    8
    7
    6

    Use a for OR a while loop.
    """
    



# ============================================================
# EXERCISE 2 – Print each character of a sentence
# ============================================================

def print_characters(text):
        for letter in text:
            print(letter)
            """
    Print each character of the string 'text', one per line.

    Example:
        print_characters("Hi!")
        H
        i
        !
    """
    



# ============================================================
# EXERCISE 3 – Print "OK" three times
# ============================================================

def print_ok_three_times():
    for i in range(3):
        print("ok")
    """
    Print the word "OK" exactly three times.
    You must use a loop.
    """



# ============================================================
# EXERCISE 4 – Print all numbers from 0 to 4
# ============================================================

def print_zero_to_four():
    for i in range(0,5):
        print(i)
    """
    Print:
    0
    1
    2
    3
    4

    Use a for loop.
    """
    



# ============================================================
# EXERCISE 5 – Print odd numbers from 1 to 9
# ============================================================

def print_odd_numbers():
    for number in range(1,10,2):
        print(number)
    """
    Print all odd numbers between 1 and 9 (included):
    1, 3, 5, 7, 9

    Use a loop.
    """
    



# ============================================================
# MANUAL TESTS (OPTIONAL)
# ============================================================

print("EX 1:")
print_ten_to_six()

print("\nEX 2:")
print_characters("Hi!")

print("\nEX 3:")
print_ok_three_times()

print("\nEX 4:")
print_zero_to_four()

print("\nEX 5:")
print_odd_numbers()
