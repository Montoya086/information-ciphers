from utils import bin_to_ascii

def bits_to_ascii(bits):
    # Check if there is a space every 8 bits, if not, add it
    bits = bits.replace(" ", "")
    spaced_bits = ' '.join(bits[i:i+8] for i in range(0, len(bits), 8))

    return bin_to_ascii.bin_to_ascii(spaced_bits)

if __name__ == "__main__":
    # Example 1
    arg = "01001000011001010110110001101100011011110010000100100001"
    res = bits_to_ascii(arg)

    print('The ascii code of the binary representation "'+ arg + '" is', res)

    # Example 2
    arg = "01001000 01100101 01101100 01101100 01101111 00100000 01110111 01101111 01110010 01101100 01100100"
    res = bits_to_ascii(arg)

    print('The ascii code of the binary representation "'+ arg + '" is', res)