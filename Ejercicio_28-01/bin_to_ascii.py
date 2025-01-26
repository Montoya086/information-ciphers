import sys

def bin_to_ascii_char(binary):
    # get the integer representation of the binary code
    pos = 0
    for i in range(len(binary)):
        # get the integer representation of the binary code, converting it to decimal
        pos += int(binary[i]) * 2**(len(binary)-i-1)
    return chr(pos)

def bin_to_ascii(binary):
    # buffer to store the ascii representation
    ascii = ""
    # split the binary representation into 7-bit chunks
    chars = binary.split(" ")
    for char in chars:
        ascii += bin_to_ascii_char(char)

    return ascii

if __name__ == "__main__":
    arg = sys.argv[1:]
    bin = ""
    if len(arg) > 1:
        for a in arg:
            bin += a + " "
    else:
        bin = arg[0]
    
    res = bin_to_ascii(bin.strip())
    print('The ascii code of the binary representation "'+ bin + '" is', res)