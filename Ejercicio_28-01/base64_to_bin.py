import sys
import complete_bin

def base64_to_bin_char(base64):
    # get the ascii code of the character
    pos = ord(base64)
    pos -= 65 # set it to 0 in base64
    # buffer to store the binary representation
    if pos < 0 or pos > 63:
        Exception("Invalid character")
    binary = ""
    # convert the ascii code to binary
    while pos > 0:
        # get the remainder of the division by 2
        binary = str(pos % 2) + binary 
        # get the integer division by 2 to continue the process
        pos = pos // 2

    return complete_bin.complete_bin(binary)

def base64_to_bin(base64):
    # buffer to store the binary representation
    binary = ""
    # iterate over the characters of the string
    for char in base64:
        # get the binary representation of the character
        binary += base64_to_bin_char(char) + " "
    return binary

if __name__ == "__main__":
    arg = sys.argv[1]
    res = base64_to_bin(arg)
    print('The binary representation of the base64 code of "'+ arg + '" is', res)