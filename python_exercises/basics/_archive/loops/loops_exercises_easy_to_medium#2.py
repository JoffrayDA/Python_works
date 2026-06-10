"""
LOOPS EXERCISES – EASY TO MEDIUM LEVEL
--------------------------------------

This file contains loop practice exercises:
- for loops
- while loops
- conditions + loops
- simple function logic

Complete the functions by replacing 'pass'.
Do NOT change the function names.
"""


# ============================================================
# EXERCISE 1 – Count from 1 to N (FOR LOOP)
# ============================================================

def count_to(n):
    """
    Prints all numbers from 1 up to n (inclusive).
    You MUST use a for loop.

    Example:
        count_to(5) prints:
        1
        2
        3
        4
        5
    """
    pass



# ============================================================
# EXERCISE 2 – Sum 1 to N (FOR LOOP + RETURN)
# ============================================================

def sum_to(n):
    """
    Returns the sum of all integers from 1 up to n.
    You must use a for loop (no built-in sum function).

    Example:
        sum_to(5) -> 15
        sum_to(10) -> 55
    """
    pass



# ============================================================
# EXERCISE 3 – Count vowels in a string (FOR LOOP + CONDITIONS)
# ============================================================

def count_vowels(text):
    """
    Counts how many vowels appear in the string 'text'.
    Vowels are: a, e, i, o, u, y (case insensitive).

    Requirements:
        - Use a for loop
        - Convert text to lowercase
        - Check each character

    Examples:
        count_vowels("hello")  -> 2
        count_vowels("PYTHON") -> 1
    """
    pass



# ============================================================
# EXERCISE 4 – Countdown using WHILE LOOP
# ============================================================

def countdown(n):
    """
    Prints a countdown from n down to 0 using a while loop.
    After reaching 0, print "GO!".

    Example:
        countdown(5) prints:
        5
        4
        3
        2
        1
        0
        GO!
    """
    pass



# ============================================================
# MANUAL TESTS (OPTIONAL)
# ============================================================

print("=== EXERCISE 1 ===")
count_to(5)

print("\n=== EXERCISE 2 ===")
print(sum_to(5))   
print(sum_to(10))  

print("\n=== EXERCISE 3 ===")
print(count_vowels("hello"))
print(count_vowels("PYTHON"))
print(count_vowels("ChatGPT"))

print("\n=== EXERCISE 4 ===")
countdown(5)
