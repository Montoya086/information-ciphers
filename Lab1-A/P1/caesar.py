# Cifrado cesar
import sys

KEY = 3

alphabet = "abcdefghijklmnñopqrstuvwxyz"

def cypher(text, key):
    # convert text to lowercase
    text = text.lower()
    # result string
    result = ""
    # iterate over each letter in the text
    for letter in text:
        # if the letter is in the alphabet
        if letter in alphabet:
            # add the padded letter to the result
            result += alphabet[(alphabet.index(letter) + key) % len(alphabet)]
        else:
            # if the letter is not in the alphabet, add it to the result
            result += letter
    return result

def decypher(text, key):
    # convert text to lowercase
    text = text.lower()
    # result string
    result = ""
    # iterate over each letter in the text
    for letter in text:
        # if the letter is in the alphabet
        if letter in alphabet:
            # add the padded letter to the result
            result += alphabet[(alphabet.index(letter) - key) % len(alphabet)]
        else:
            # if the letter is not in the alphabet, add it to the result
            result += letter
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2 or (sys.argv[1] != "-d" and sys.argv[1] != "-c"):
        print("Usage: python caesar.py <-d|-c> (d: decypher, c: cypher)")
        sys.exit(1)
    
    mode = sys.argv[1]

    if mode == "-c":
        text = input("Enter the text to cypher: ")
        print("\n Cyphered text: ", cypher(text, KEY))
    elif mode == "-d":
        text = input("Enter the text to decypher: ")
        print("\n Decyphered text: ", decypher(text, KEY))


