"""Write a function reverse_text(text) that returns the string reversed."""
print("----Exercice 1----")
def reverse_text(text):
    return text[::-1]
print(reverse_text("Hello my friend."))

"""Write a function count_even(numbers) that:takes a list of numbers
returns how many of them are even"""
print("----Exercice 2----")
def count_even(numbers):
    count = 0 
    for n in numbers: 
        if n % 2 == 0: 
            count += 1 
    return count
print(count_even([1,2,3,4,5,6,7,8,9,10,11,12,13,14444]))

"""Write a function find_min(numbers) that returns the smallest value in the list,
without using min()."""
print("----Exercice 3----")
def find_min(numbers):
    smallest = numbers[0]

    for n in numbers : 
        if n < smallest : 
            smallest = n 
    return smallest
print(find_min([5, 9, 2, 8, 32]))

"""Write a function is_sorted(numbers) that returns: True if the list is sorted in ascending order
False otherwise"""
print("----Exercice 4----")
def is_sorted(numbers):
    for x, y in zip(numbers, numbers[1:]):
        if x > y:
            return False
    return True 

"""Write a function replace_char(text, old, new) that: replaces all occurrences of old with new
without using .replace()"""
print("----Exercice 5----")
def replace_chart(text, old, new):
    result = ""
    for char in text:
        if char == old:
            result += new
        else:
            result += char
    return result


