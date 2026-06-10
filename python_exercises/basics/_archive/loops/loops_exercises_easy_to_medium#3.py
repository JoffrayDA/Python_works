print("-----1st exercice------")
def print_multiples_of_three():
    """
    Print all numbers between 50 and 60 (inclusive)
    that are divisible by 3.

    Expected output:
        51
        54
        57
        60
    """
    for n in range(50,61):
        if n % 3 == 0 :
            print(n)
print_multiples_of_three()

print("-----2nd exercice------")
def count_uppercase(text):
    """
    Return how many characters inside 'text' are uppercase.

    Example:
        "HeLLo" -> 3 uppercase letters
    """
    count = 0
    for char in text : 
        if char.isupper():
            count += 1
    return count

print(count_uppercase("HeLLo"))

print("-----3rd exercice------")
def print_until_over_100(numbers):
    """
    Print numbers one by one.
    STOP when a number is strictly greater than 100.

    Example:
        [5, 9, 200, 7] -> prints 5, 9, STOP
    """
    for n in numbers:
        if n > 100 : 
            break
        print(n)

print(print_until_over_100([5, 9, 90, 7, 151, 7]))

print("-----4th exercice------")
def filter_positive(numbers):
    """
    Return a NEW list containing only the positive numbers.

    Example:
        [-4, 3, 0, 12, -1] -> [3, 12]
    """
    result = []
    for n in numbers : 
        if n > 0 :
            result.append(n)
    return result

print(filter_positive([5, 9, 90, -7, 151, 7]))

print("-----5th exercice------")
def count_digits(text):
    """
    Return how many characters inside 'text' are digits (0-9).

    Example:
        "a1b22c" -> 3 digits
    """
    count = 0
    for d in text : 
        if d.isdigit():
            count += 1 
    return count

print(count_digits("a4fd6f48b4grf1"))


