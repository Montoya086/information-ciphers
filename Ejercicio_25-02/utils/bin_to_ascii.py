import sys

def bin_to_ascii_char(binary, verbose=False):
    # get the integer representation of the binary code
    pos = 0
    for i in range(len(binary)):
        # get the integer representation of the binary code, converting it to decimal
        pos += int(binary[i]) * 2**(len(binary)-i-1)
    if verbose:
        print("Binary:", binary, "Decimal:", pos, "ASCII:", chr(pos))
    return chr(pos)

def bin_to_ascii(binary, verbose=False):
    # buffer to store the ascii representation
    ascii = ""
    # split the binary representation into 8-bit chunks
    chars = binary.split(" ")
    if verbose:
        print("Binary chunks:", chars)
    for char in chars:
        ascii += bin_to_ascii_char(char, verbose)

    return ascii

if __name__ == "__main__":
    bin = "01001000 01100101 01101100 01101100 01101111"
    res = bin_to_ascii(bin)
    print('The ascii code of the binary representation "'+ bin + '" is', res)