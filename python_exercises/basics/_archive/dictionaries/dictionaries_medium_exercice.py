print("---Exercice1---")
def key_of_max_value(d):
    """
    Exemple : {"a":3, "b":9, "c":2} → "b"
    """
    max_key = None
    max_value = None

    for k, v in d.items():
        if max_value is None or v > max_value:
            max_value = v
            max_key = k

    return max_key

print(key_of_max_value({"a": 3, "b": 9, "c": 2}))

print("---Exercice2---")
def make_dict(keys, values):
    result = {}
    index = 0

    for k in keys:
        result[k] = values[index]
        index += 1
    
    return result

keys = ["a", "z", "e", "r"]
values = [1, 2, 3, 4]

print(make_dict(keys, values))

print("---Exercice3---")
def char_types(text):
    result = {
        "letters": 0,
        "digits": 0,
        "spaces": 0,
        "others": 0
    }

    for c in text:
        if c.isalpha():
            result["letters"] += 1
        elif c.isdigit():
            result["digits"] += 1
        elif c == " ":
            result["spaces"] += 1
        else:
            result["others"] += 1

    return result
print(char_types("Bonjour 123 !"))

print("---Exercice4---")
def dict_product(d):
    product = 1
    for v in d.values():
        product *= v
    return product

d = {"a": 2, "b": 3, "c": 4}

print(dict_product(d))

print("---Exercice5---")
def keys_with_even_values(d):
    result = []
    for k, v in d.items():
        if v % 2 == 0:
            result.append(k)
    return result

d = {"a": 2, "b": 3, "c": 4, "d": 5}

print(keys_with_even_values(d))