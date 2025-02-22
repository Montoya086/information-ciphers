from utils import ascii_to_bin, bin_to_ascii, xor_bin
from keygen import generate_key
def ascii_xor_ascii (ascii, key, verbose=False):
    ascii_bin = ascii_to_bin.ascii_to_bin(ascii, verbose)
    key_bin = ascii_to_bin.ascii_to_bin(key, verbose)
    xor = xor_bin.xor_bin(ascii_bin, key_bin, verbose).strip()
    cyphered = bin_to_ascii.bin_to_ascii(xor, verbose)
    return cyphered

def cypher(plain_text, nonce, verbose=False):
    key = generate_key(len(plain_text), nonce)
    return ascii_xor_ascii(plain_text, key, verbose)

def decypher(cyphered, nonce, verbose=False):
    key = generate_key(len(cyphered), nonce)
    return ascii_xor_ascii(cyphered, key, verbose)

