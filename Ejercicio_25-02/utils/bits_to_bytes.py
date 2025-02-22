def bits_to_bytes(bits):
    bits = bits.replace(" ", "")
    return bytes(int(bits[i:i+8], 2) for i in range(0, len(bits), 8))