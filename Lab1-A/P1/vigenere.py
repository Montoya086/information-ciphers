# vigenere cipher
import sys

alphabet = "abcdefghijklmnñopqrstuvwxyz"

vigenere_table = dict()
#fill the vigenere table
for i in range(len(alphabet)):
    # create a new dictionary for each letter in the alphabet
    vigenere_table[alphabet[i]] = dict()
    # fill the dictionary with the vigenere cipher
    for j in range(len(alphabet)):
        vigenere_table[alphabet[i]][alphabet[j]] = alphabet[(i+j) % len(alphabet)]

"""
    Table structure:
    {
        'a': {'a': 'a', 'b': 'b', 'c': 'c', ..., 'z': 'z', ' ': ' '},
        'b': {'a': 'b', 'b': 'c', 'c': 'd', ..., 'z': 'a', ' ': 'b'},
        ...
        ' ': {'a': ' ', 'b': 'a', 'c': 'b', ..., 'z': 'm', ' ': 'n'}
    }
"""

def cypther(text, key):
    # convert text to lowercase
    text = text.lower()
    # result string
    result = ""
    # iterate over each letter in the text
    for i in range(len(text)):
        # add the padded letter to the result
        result += vigenere_table[text[i]][key[i%len(key)]]
    return result

def decypher(text, key):
    # convert text to lowercase
    text = text.lower()
    # result string
    result = ""
    # iterate over each letter in the text
    for i in range(len(text)):
        # add the padded letter to the result
        for letter in vigenere_table[key[i%len(key)]]:
            if vigenere_table[key[i%len(key)]][letter] == text[i]:
                result += letter
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2 or (sys.argv[1] != "-d" and sys.argv[1] != "-c"):
        print("Usage: python afin.py <-d|-c> (d: decypher, c: cypher)")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == "-c":
        text = input("\nEnter the text to cypher: ")
        key = input("\nEnter the key: ")
        print("\n Cyphered text:", cypther(text, key))
    
    elif mode == "-d":
        text = input("\nEnter the text to decypher: ")
        key = input("\nEnter the key: ")
        print("\n Decyphered text:", decypher(text, key))