import sys

def bin_to_base64_char(binary):
    # get the integer representation of the binary code
    pos = int(binary, 2)
    pos += 65 # set it to 0 in base64
    if pos < 65 or pos > 90:
        Exception("Invalid character")
    return chr(pos)

def bin_to_base64(binary):
    # buffer to store the base64 representation
    base64 = ""
    # split the binary representation into 8-bit chunks
    chars = binary.split(" ")
    for char in chars:
        base64 += bin_to_base64_char(char)

    return base64

if __name__ == "__main__":
    arg = sys.argv[1:]
    bin = ""
    if len(arg) > 1:
        for a in arg:
            bin += a + " "
    else:
        bin = arg[0]
    
    res = bin_to_base64(bin.strip())
    print('The base64 code of the binary representation "'+ bin + '" is', res)