from collections import Counter

alphabet = "abcdefghijklmnñopqrstuvwxyz"

theorical_freq = {
    "a": 0.1253,
    "b": 0.0142,
    "c": 0.0468,
    "d": 0.0586,
    "e": 0.1368,
    "f": 0.0069,
    "g": 0.0101,
    "h": 0.0070,
    "i": 0.0625,
    "j": 0.0044,
    "k": 0.0002,
    "l": 0.0497,
    "m": 0.0315,
    "n": 0.0671,
    "ñ": 0.0031,
    "o": 0.0868,
    "p": 0.0251,
    "q": 0.0088,
    "r": 0.0687,
    "s": 0.0798,
    "t": 0.0463,
    "u": 0.0291,
    "v": 0.0111,
    "w": 0.0008,
    "x": 0.0022,
    "y": 0.0088,
    "z": 0.0047
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
