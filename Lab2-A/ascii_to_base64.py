from utils import ascii_to_bin, bin_to_base64

def ascii_to_base64(ascii):
    return bin_to_base64.bin_to_base64(ascii_to_bin.ascii_to_bin(ascii, True), True)

if __name__ == "__main__":
    # Example 1
    arg = "Hello!!"
    res = ascii_to_base64(arg)

    print('The base64 representation of the ASCII code of "'+ arg + '" is', res)

    # Example 2
    arg = "Hello world"
    res = ascii_to_base64(arg)

    print('The base64 representation of the ASCII code of "'+ arg + '" is', res)