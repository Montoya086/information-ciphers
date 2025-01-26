import sys
import complete_bin

def ascii_to_bin_char(ascii):
    # get the ascii code of the character
    pos = ord(ascii)
    # buffer to store the binary representation
    binary = ""
    # convert the ascii code to binary
    while pos > 0:
        # get the remainder of the division by 2
        binary = str(pos % 2) + binary
        # get the integer division by 2 to continue the process
        pos = pos // 2

    return complete_bin.complete_bin(binary)

def ascii_to_bin(ascii):
    # buffer to store the binary representation
    binary = ""
    # iterate over the characters of the string
    for char in ascii:
        # get the binary representation of the character
        binary += ascii_to_bin_char(char) + " "
    return binary


if __name__ == "__main__":
    arg = sys.argv[1]
    res = ascii_to_bin(arg)
    print('The binary representation of the ASCII code of "'+ arg + '" is', res)