import sys
import complete_bin

# Function to perform the XOR operation
def xor (a, b):
    return a ^ b

def xor_bin(bin1, bin2):
    # buffer to store the xor operation
    res = ""
    # split the binary representation into 8-bit chunks
    chars1 = bin1.split(" ")
    chars2 = bin2.split(" ")
    for i in range(len(chars1)):
        # get the integer representation of the binary code
        int_chars1 = int(chars1[i])
        int_chars2 = int(chars2[i])
        # perform the XOR operation
        res += complete_bin.complete_bin(str(xor(int_chars1, int_chars2))) + " "
    return res

if __name__ == "__main__":
    arg1 = "00100000 00100001"
    arg2 = "00000001 00100011"
    res = xor_bin(arg1, arg2)
    print('The XOR operation of the binary representations "'+ arg1 + '" and "' + arg2 + '" is', res)