import sys

def ascii_to_bin(ascii):
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

    return binary


if __name__ == "__main__":
    arg = sys.argv[1]
    res = ascii_to_bin(arg)
    print('The binary representation of the ASCII code of', arg, 'is', res)