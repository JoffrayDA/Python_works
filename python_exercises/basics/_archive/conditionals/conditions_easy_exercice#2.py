def number_type(n):
    """
    Takes a number n and returns:
    - "positive" if n > 0
    - "negative" if n < 0
    - "zero"     if n == 0
    """
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    elif n==0:
        return "zero"
    
print(number_type(-5))
print(number_type(-1))
print(number_type(0))
print(number_type(2))
print(number_type(54))
