from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def add_padding(data):
    block_size = 8  #DES block size is 8 bytes
    padding_length = block_size - (len(data) % block_size)

    if padding_length != 0:
        print(f"Padding needed: {padding_length}")

    #create padding
    padding_bytes = []
    #the padding is the padding length for more security and uniformity
    padding = padding_length
    for i in range(padding_length):
        #append the padding to the padding bytes
        padding_bytes.append(padding)
    
    #parse the padding bytes to bytes
    padded_data = bytearray(data)
    #extend the padding bytes to the data
    padded_data.extend(padding_bytes)
    print(f"Padded data: {padded_data}")
    return bytes(padded_data)

def remove_padding(padded_data):
    #convert to bytearray for easier manipulation
    data = bytearray(padded_data)
    
    #get the padding length from the last byte
    padding_length = data[-1]
    
    #verify the padding is valid
    for i in range(1, padding_length + 1):
        if data[-i] != padding_length:
            raise ValueError("Invalid padding")
    
    #remove the padding
    return bytes(data[:-padding_length])

def encrypt_des(plaintext, key=None):
    if key is None:
        key = get_random_bytes(8)
    
    #convert the string to bytes and apply padding
    data = add_padding(plaintext.encode('utf-8'))
    
    #create the cipher object and encrypt
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(data)
    
    return ciphertext, key

def decrypt_des(ciphertext, key):
    #create the cipher object
    cipher = DES.new(key, DES.MODE_ECB)
    
    #decrypt and remove padding
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = remove_padding(padded_plaintext)
    
    return plaintext.decode('utf-8')

if __name__ == "__main__":
    #test the encryption and decryption
    with open("des.txt", "r") as file:
        message = file.read()
    print("Original message:", message)
    key = get_random_bytes(8)
    
    #encrypt
    encrypted_data, key = encrypt_des(message, key)
    print("Encrypted (hex):", encrypted_data.hex())
    print("Key (hex):", key.hex())
    
    #decrypt
    decrypted_message = decrypt_des(encrypted_data, key)
    print("Decrypted message:", decrypted_message)
