chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/" # Base64 characters

def bin_to_base64(binary):
    # remove spaces if they exist
    binary = binary.replace(" ", "")
    
    # pad with zeros to make length multiple of 6
    padding_length = (6 - len(binary) % 6) % 6
    binary = binary + "0" * padding_length
    
    base64 = ""
    # process 6 bits at a time
    for i in range(0, len(binary), 6):
        chunk = binary[i:i+6]
        # convert binary chunk to decimal
        val = 0
        for bit in chunk:
            val = (val << 1) | (int(bit))
        #get corresponding base64 character
        base64 += chars[val]
    
    #add padding if needed
    padding = "=" * ((4 -len(base64) %4) %4)
    return base64 + padding

if __name__ == "__main__":
    bin = "01001000 01101111 01101100 01100001"
    res = bin_to_base64(bin)
    print('The base64 code of the binary representation "'+ bin + '" is', res)