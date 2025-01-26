import ascii_to_bin
import bin_to_ascii
import xor_bin
import dynamic_key_gen

def cypher_ascii_static(text, key):
    dynamic_key = dynamic_key_gen.dynamic_key_gen(key, len(text))
    # get the binary representation of the key and the text
    key_bin = ascii_to_bin.ascii_to_bin(dynamic_key)
    # get the binary representation of the text
    text_bin = ascii_to_bin.ascii_to_bin(text)
    # get the xor of the text and the key
    res = xor_bin.xor_bin(text_bin, key_bin)
    return bin_to_ascii.bin_to_ascii(res)


if __name__ == "__main__":
    text = "Hello!!"
    key = "key"
    res = cypher_ascii_static(text, key)
    print('The cyphered text of "'+ text + '" with the key "'+ key + '" is', res)