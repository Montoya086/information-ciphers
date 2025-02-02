# afin cypher
import sys
from clean import clean_text

alphabet = "abcdefghijklmnñopqrstuvwxyz"

# greatest common divisor
def mcd(a, m):
    """
    Source: ClaudeIA
    Promt: how to calculate the greatest common divisor of two numbers in Python
    """
    while m:
        a, m = m, a % m
    return a

def cypher(text, a, b):
    # convert text to lowercase
    text = text.lower()
    # result string
    res = ""
    # iterate over each letter in the text
    for letter in text:
        # if the letter is in the alphabet
        if letter in alphabet:
            # add the padded letter to the result
            res += alphabet[(a * alphabet.index(letter)+ b) % len(alphabet)]
        else:
            # if the letter is not in the alphabet, add it to the result
            res +=letter

    return res

def mod_inverse(a, m):
    for x in range(1, m):
        # if the product of a and x modulo m is equal to 1, return x
        if ((a % m)*(x % m)) % m ==1:
            return x
    return None

def decypher(text, a, b):
    # convert text to lowercase
    text = text.lower()
    # result string
    res = ""
    a_inv = mod_inverse(a, len(alphabet))
    # iterate over each letter in the text
    for letter in text:
        # if the letter is in the alphabet
        if letter in alphabet:
            # add the padded letter to the result
            res += alphabet[(a_inv *(alphabet.index(letter) -b)) % len(alphabet)]
        else:
            # if the letter is not in the alphabet, add it to the result
            res += letter
    return res
    

def validate_key(key):
    if mcd(key, len(alphabet)) != 1:
        print("\nThe key should be coprime with the length of the alphabet")
        sys.exit(1)
    

if __name__ == "__main__":
    if len(sys.argv) != 2 or (sys.argv[1] != "-d" and sys.argv[1] != "-c"):
        print("Usage: python afin.py <-d|-c> (d: decypher, c: cypher)")
        sys.exit(1)

    mode = sys.argv[1]

    a = 0
    b = 0
    try :
        a = int(input("\nEnter a: "))
        b = int(input("\nEnter b: "))    
    except ValueError:
        print("\nThe key should be an integer")
        sys.exit(1)
    validate_key(a)

    if mode == "-c":
        text = input("\nEnter the text to cypher: ")
        text = clean_text(text, alphabet)
        print("\n Cyphered text:", cypher(text, a, b))
    elif mode == "-d":
        text = input("\nEnter the text to decypher: ")
        text = clean_text(text, alphabet)
        print("\n Decyphered text:", decypher(text, a, b))
