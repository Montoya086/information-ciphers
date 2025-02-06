from utils import ascii_to_bin, bin_to_ascii, dynamic_key_gen, xor_bin

def ascii_xor_ascii (ascii, key):
    if len(ascii) < len(key):
        key = key[:len(ascii)]
    elif len(ascii) > len(key):
        key = dynamic_key_gen.complete_key(key, len(ascii))
    ascii_bin = ascii_to_bin.ascii_to_bin(ascii, True)
    key_bin = ascii_to_bin.ascii_to_bin(key, True)
    xor = xor_bin.xor_bin(ascii_bin, key_bin, True)
    return bin_to_ascii.bin_to_ascii(xor, True)

if __name__ == "__main__":
    # Example 1
    arg1 = "Hello!!"
    arg2 = "key"
    res = ascii_xor_ascii(arg1, arg2)

    print('The XOR of the ASCII code of "'+ arg1 + '" with the ASCII code of "'+ arg2 + '" is', res)

    # Example 2
    arg1 = "Hello world"
    arg2 = "keyssssssssssss"
    res = ascii_xor_ascii(arg1, arg2)

    print('The XOR of the ASCII code of "'+ arg1 + '" with the ASCII code of "'+ arg2 + '" is', res)
