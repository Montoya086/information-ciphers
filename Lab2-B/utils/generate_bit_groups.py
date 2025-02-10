def generate_bit_groups(bits):
    res = ' '.join(bits[i:i+8] for i in range(0, len(bits), 8)).strip()
    return res