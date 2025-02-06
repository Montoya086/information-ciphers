import sys
from utils import complete_bin

# Function to perform the XOR operation
def xor (a, b):
    return a ^ b

def xor_bin(bin1, bin2):
    # buffer to store the xor operation
    retval = ""
    # split the binary representation into 8-bit chunks
    chars1 = bin1.split(" ")
    chars2 = bin2.split(" ")
    for i in range(len(chars1)):
        # get the integer representation of the binary code
        str_chars1 = str(chars1[i])
        str_chars2 = str(chars2[i])
        part_res = ""
        for j in range(8):
            int_chars1 = int(str_chars1[j])
            int_chars2 = int(str_chars2[j])
            # perform the XOR operation
            part_res += str(xor(int_chars1, int_chars2))
        retval += part_res + " "
    return complete_bin.complete_bin(retval)

if __name__ == "__main__":
    arg1 = "00100000 00100001"
    arg2 = "00000001 00100011"
    res = xor_bin(arg1, arg2)
    print('The XOR operation of the binary representations "'+ arg1 + '" and "' + arg2 + '" is', res)