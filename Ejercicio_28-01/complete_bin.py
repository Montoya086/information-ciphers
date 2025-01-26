# Script to add the 0's to the left of the binary representation of the base64 code

def complete_bin(binary):
    # get the length of the binary representation
    length = len(binary)
    # calculate the number of 0's to add
    zeros = 6 - length
    # add the 0's to the left
    for _ in range(zeros):
        binary = "0" + binary
    return binary