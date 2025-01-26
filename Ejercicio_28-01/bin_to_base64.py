def bin_to_base64_char(binary):
    # get the integer representation of the binary code
    pos = 0
    for i in range(len(binary)):
        # get the integer representation of the binary code, converting it to decimal
        pos += int(binary[i]) * 2**(len(binary)-i-1)
    
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
    bin = "00000000 00000001"
    res = bin_to_base64(bin)
    print('The base64 code of the binary representation "'+ bin + '" is', res)