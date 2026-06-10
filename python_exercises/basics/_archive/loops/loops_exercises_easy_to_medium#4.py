print("-----1st exercice------")
def count_negative(numbers):
    """
    Return how many numbers in the list are strictly negative.

    Example:
        [-5, 3, -1, 0, 12] -> 2
    """
    count = 0
    for n in numbers: 
        if n < 0:
            count += 1
    return count 

print(count_negative([-5, 3, -1, 0, 12]))

print("-----2nd exercice------")
def print_no_spaces(text):
    """
    Print each character of the string except spaces.

    Example:
        "a b c" -> prints a, b, c each on a new line.
    """
    for char in text: 
        if char != " ":
            print(char)
print_no_spaces("Hello my friend ")

print("-----3rd exercice------")
def print_until_divisible_by_seven(n):
    """
    Print numbers starting from 1.
    STOP as soon as a number divisible by 7 appears.

    Example:
        n = 20 -> prints 1,2,3,4,5,6 then STOP.
    """
    for i in range(1, n+1):
        if i % 7 == 0 :
            break
        print(i)
print_until_divisible_by_seven(20)

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
    for n in numbers :
        total +=n
        count +=1
    
    if count == 0:
        return 0
    
    return total/count
print(compute_average([4, 6, 10]))  

print("-----5th exercice------")
def contains_digit(text):
    """
    Return True if at least ONE character in the string is a digit (0–9).
    Otherwise return False.

    Example:
        "abc5d" -> True
        "hello" -> False
    """
    for d in text :
        if d.isdigit():
            return True 
        return False 
print(contains_digit("abc5fd4fsd4d"))
