# ============================================================
# EXERCISE 1 – Print numbers from 1 to 5
# ============================================================

def print_one_to_five():
    for n in range(1,6):
        print(n)
    """
    Print:
    1
    2
    3
    4
    5

    Use a for loop.
    """
    

# ============================================================
# EXERCISE 2 – Print each word of a sentence
# ============================================================

def print_words(sentence):
    for word in sentence.split():
        print(word)
    """
    Print each word of the sentence on a new line.

    Example:
        print_words("Hello world")
        Hello
        world
    """
    

# ============================================================
# EXERCISE 3 – Print "Python is cool" 4 times
# ============================================================

def repeat_python():
    for i in range(4):
        print("Python is cool")
    """
    Print the sentence:
    "Python is cool"
    exactly 4 times.

    Use a loop.
    """


# ============================================================
# EXERCISE 4 – Print numbers from 5 down to 1
# ============================================================

def countdown_five_to_one():
    n=5
    while n >0:
        print(n)
        n = n-1
    """
    Print:
    5
    4
    3
    2
    1

    Use a while loop OR a for loop with reverse range.
    """
    

# ============================================================
# EXERCISE 5 – Print the characters at EVEN positions
# ============================================================

def print_even_index_characters(text):
    for i in range(0, len(text), 2):
        print(text[i])
    """
    Print only the characters that are at even positions (0, 2, 4, ...).

    Example:
        text = "Python"
        Output:
        P
        t
        o

    Use a loop and index checking.
    """


# ============================================================
# MANUAL TESTS (OPTIONAL)
# ============================================================

print("EX 1:")
print_one_to_five()

print("\nEX 2:")
print_words("I love Python")

print("\nEX 3:")
repeat_python()

print("\nEX 4:")
countdown_five_to_one()

print("\nEX 5:")
print_even_index_characters("Python")
