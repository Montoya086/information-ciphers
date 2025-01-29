import sys
import base64_to_bin
import bin_to_ascii

def base64_to_ascii(base64):
    # get the binary representation of the base64 code
    binary = base64_to_bin.base64_to_bin(base64)
    print(binary)
    # get the ascii representation of the binary code
    return bin_to_ascii.bin_to_ascii(binary)

if __name__ == "__main__":
    arg = "SG9sYQ=="
    res = base64_to_ascii(arg)
    print('The ascii code of the base64 representation "'+ arg + '" is', res)