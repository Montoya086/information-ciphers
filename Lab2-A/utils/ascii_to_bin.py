import sys
from utils import complete_bin

def ascii_to_bin_char(ascii, verbose=False):
    # get the ascii code of the character
    if verbose:
        print(f"Getting the ASCII code of '{ascii}'")
    pos = ord(ascii)
    if verbose:
        print(f"The ASCII code of '{ascii}' is {pos}")
    # buffer to store the binary representation
    binary = ""
    # convert the ascii code to binary
    while pos > 0:
        if verbose:
            print(f"Getting the remainder of {pos} divided by 2")
        # get the remainder of the division by 2
        binary = str(pos % 2) + binary
        # get the integer division by 2 to continue the process
        pos = pos // 2
    if verbose:
        print(f"The binary representation of the ASCII code of '{ascii}' is {binary}")

    return complete_bin.complete_bin(binary)

def ascii_to_bin(ascii, verbose=False):
    # buffer to store the binary representation
    binary = ""
    # iterate over the characters of the string
    for char in ascii:
        if verbose:
            print(f"Converting '{char}' to binary")
        # get the binary representation of the character
        binary += ascii_to_bin_char(char) + " "
    return binary.strip()


if __name__ == "__main__":
    arg = "Hello!!"
    res = ascii_to_bin(arg)
    print('The binary representation of the ASCII code of "'+ arg + '" is', res)