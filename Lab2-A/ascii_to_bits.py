from utils import ascii_to_bin

def ascii_to_bits (ascii):
    return ascii_to_bin.ascii_to_bin(ascii).replace(" ", "")

if __name__ == "__main__":
    # Example 1
    arg = "Hello!!"
    res = ascii_to_bits(arg)

    print('The binary representation of the ASCII code of "'+ arg + '" is', res)

    # Example 2
    arg = "Hello world"
    res = ascii_to_bits(arg)

    print('The binary representation of the ASCII code of "'+ arg + '" is', res)