import ascii_to_bin
import xor_bin
import dynamic_key_gen

def cypher_ascii_dynamic(text, keylength):
    dynamic_key = dynamic_key_gen.dynamic_key_gen(keylength)
    if len(text) < keylength:
        padding = len(text) % keylength
        if padding != 0:
            text += " " * (keylength - padding)
    else:
        dynamic_key = dynamic_key_gen.complete_key(dynamic_key, len(text))
    # get the binary representation of the key and the text
    key_bin = ascii_to_bin.ascii_to_bin(dynamic_key)
    # get the binary representation of the text
    text_bin = ascii_to_bin.ascii_to_bin(text)
    # get the xor of the text and the key
    res = xor_bin.xor_bin(text_bin, key_bin)
    return res, dynamic_key, text_bin, key_bin


if __name__ == "__main__":
    text = "Hello!!"
    keyLen = 10
    res, key, text_bin, key_bin = cypher_ascii_dynamic(text, keyLen)
    print(f'The cyphered text of "{text}" ({text_bin})\nwith the key "{key}" ({key_bin})\nis', res)