from collections import Counter

alphabet = "abcdefghijklmnñopqrstuvwxyzáéíóúü"

theorical_freq = {
    'a': 0.11525,
    'b': 0.02215,
    'c': 0.04019,
    'd': 0.05010,
    'e': 0.12181,
    'f': 0.00692,
    'g': 0.01768,
    'h': 0.00703,
    'i': 0.06247,
    'j': 0.00493,
    'k': 0.00011,
    'l': 0.04967,
    'm': 0.03157,
    'n': 0.06712,
    'o': 0.08683,
    'p': 0.02510,
    'q': 0.00877,
    'r': 0.06871,
    's': 0.07977,
    't': 0.04632,
    'u': 0.02927,
    'v': 0.01138,
    'w': 0.00017,
    'x': 0.00215,
    'y': 0.01008,
    'z': 0.00467,
    'á': 0.00502,
    'é': 0.00433,
    'í': 0.00725,
    'ñ': 0.00311,
    'ó': 0.00827,
    'ú': 0.00168,
    'ü': 0.00012
}

def clean_text(text):
    # remove all characters that are not in the alphabet
    return "".join([char for char in text.lower() if char in alphabet])

def calc_relative_freq(text):
    counter = Counter(text)
    total = sum(counter.values())
    
    # calculate the relative frequency of each character
    frequencies = {char: count/total for char, count in counter.items()}

    # fill the frequencies dictionary with the alphabet
    for char in alphabet:
        if char not in frequencies:
            frequencies[char] = 0
            
    return frequencies

def open_file(filename):
    with open(filename, "r") as file:
        return file.read()
    
def calculate_prob_dist(expected_freq, observed_freq):
    res = 0
    for char in observed_freq:
        observed = observed_freq[char]
        expected = expected_freq[char]
        if expected > 0: # avoid division by zero
            res += ((observed - expected) ** 2) / expected
    return res
