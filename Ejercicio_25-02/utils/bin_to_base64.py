chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/" # Base64 characters

def bin_to_base64(binary, verbose=False):
    # remove spaces if they exist
    binary = binary.replace(" ", "")
    
    # pad with zeros to make length multiple of 6
    padding_length = (6 - len(binary) % 6) % 6
    if verbose:
        print("Padding length:", padding_length)
    binary = binary + "0" * padding_length

    if verbose:
        print("Padded binary:", binary)
    
    base64 = ""
    # process 6 bits at a time
    if verbose:
        print("Processing 6 bits at a time")
    for i in range(0, len(binary), 6):
        chunk = binary[i:i+6]
        if verbose:
            print("Chunk:", chunk)
        # convert binary chunk to decimal
        val = 0
        for bit in chunk:
            if verbose:
                print("Bit:", bit)
            val = (val << 1) | (int(bit))
        #get corresponding base64 character
        if verbose:
            print("Decimal value:", val)
        base64 += chars[val]

        if verbose:
            print("Base64 character:", chars[val])
    
    #add padding if needed
    padding = "=" * ((4 -len(base64) %4) %4)
    if verbose:
        print("Padding:", padding)
    return base64 + padding

if __name__ == "__main__":
    bin = "01001000 01101111 01101100 01100001"
    res = bin_to_base64(bin)
    print('The base64 code of the binary representation "'+ bin + '" is', res)