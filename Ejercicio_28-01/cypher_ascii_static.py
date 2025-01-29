import ascii_to_bin
import bin_to_ascii
import xor_bin
import dynamic_key_gen

def cypher_ascii_static(text, key):
    if len(text) < len(key):
        padding = len(text) % len(key)
        if padding != 0:
            text += " " * (len(key) - padding)
    else:
        key = dynamic_key_gen.complete_key(key, len(text))
    # get the binary representation of the key and the text
    key_bin = ascii_to_bin.ascii_to_bin(key)
    # get the binary representation of the text
    text_bin = ascii_to_bin.ascii_to_bin(text)
    # get the xor of the text and the key
    res = xor_bin.xor_bin(text_bin, key_bin)
    return res, key, key_bin, text_bin
    # devolver binario


if __name__ == "__main__":
    text = "Hello!!"
    key = "exa"
    res, newKey, key_bin, text_bin = cypher_ascii_static(text, key)
    print(f'The cyphered text of "{text}" ({text_bin})\nwith the key "{newKey}" ({key_bin})\nis', res)