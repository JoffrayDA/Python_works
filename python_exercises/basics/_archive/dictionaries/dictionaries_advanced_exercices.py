print("---Exercice1---")
def make_dict(keys, values):
    result = {}
    index = 0

    for k in keys:
        result[k] = values[index]
        index += 1

    return result

print("---Exercice3---")
def letter_frequency(text):
    freq = {}
    text = text.lower()

    for c in text:
        if "a" <= c <= "z":        # garde seulement les lettres
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

    return freq

print("---Exercice4---")
def invert_dict(d):
    result = {}
    for k, v in d.items():
        result[v] = k
    return result

def merge_dicts(d1, d2):
    result = {}

    for k in d1:
        result[k] = d1[k]

    for k in d2:
        result[k] = d2[k]   # d2 écrase d1

    return result

print("---Exercice5---")
def filter_dict(d, n):
    result = {}
    for k, v in d.items():
        if v > n:
            result[k] = v
    return result
