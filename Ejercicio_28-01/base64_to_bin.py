chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/" # Base64 characters

def base64_to_bin(base64):
    binary = ""
    #remove padding if exists
    base64 = base64.rstrip("=")
    for char in base64:
        # get the index of the character in the base64 chars string
        val = chars.index(char)
        #convert to 6-bit binary manually
        for i in range(5, -1, -1):  # 6 bits, from position 5 to 0
            bit = (val >> i) & 1 #get each bit using right shift and mask
            binary += str(bit)
    
    #remove padding bits
    padding_length = len(binary) % 8
    if padding_length != 0:
        binary = binary[:-padding_length]
    
    # split the binary representation into 8-bit chunks
    chunks = []
    for i in range(0, len(binary), 8):
        chunks.append(binary[i:i+8])
    binary = " ".join(chunks)
            
    return binary

if __name__ == "__main__":
    arg = "SG9sYQ=="
    res = base64_to_bin(arg)
    print('The binary representation of the base64 code of "'+ arg + '" is', res)