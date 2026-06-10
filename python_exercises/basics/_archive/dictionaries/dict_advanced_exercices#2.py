print("---Exercice 1---")

def word_length_dict(words):
    """
    Exemple :
    ["apple", "hi", "python"] → {"apple":5, "hi":2, "python":6}
    """
    result = {}
    for w in words:
        result[w] = len(w)
    return result

print(word_length_dict(["apple", "hi", "python"]))

print("\n---Exercice 2---")
def sum_values_starting_with_vowel(d):
    """
    Exemple :
    {"apple":3, "banana":5, "orange":2} → 3 + 2 = 5
    """
    vowels = "aeiouyAEIOUY"
    total = 0

    for k, v in d.items():
        if k[0] in vowels:
            total += v

    return total

example_dict = {"apple": 3, "hi": 5, "python": 10, "orange": 2}
print(sum_values_starting_with_vowel(example_dict))

print("\n---Exercice 3---")
def common_keys(d1, d2):
    """
    Exemple :
    {"a":1, "b":2}, {"b":5, "c":9} → ["b"]
    """
    result = []
    for k in d1:
        if k in d2:
            result.append(k)
    return result

print(common_keys({"a":1, "b":2}, {"b":5, "c":9}))

print("\n---Exercice 4---")
def letter_count_per_word(words):
    """
    Exemple :
    ["hi", "hello"]
    →
    {
        "hi": {"h":1, "i":1},
        "hello":{"h":1,"e":1,"l":2,"o":1}
    }
    """
    result = {}

    for word in words:
        freq = {}

        for c in word:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        result[word] = freq

    return result

print(letter_count_per_word(["hi", "hello", "papa"]))

print("\n---Exercice 5---")
def keys_of_min_value(d):
    """
    Exemple :
    {"a":3, "b":1, "c":1, "d":4} → ["b","c"]
    """
    min_value = None
    for v in d.values():
        if min_value is None or v < min_value:
            min_value = v

    result = []
    for k, v in d.items():
        if v == min_value:
            result.append(k)

    return result

print(keys_of_min_value({"a":3, "b":1, "c":1, "d":4}))
