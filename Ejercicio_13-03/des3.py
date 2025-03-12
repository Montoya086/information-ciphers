from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def generate_valid_key():
    while True:
        try:
            #generate a random 24-byte key
            key = get_random_bytes(24)
            #verify the key is valid for 3DES
            DES3.new(key, DES3.MODE_CBC)
            return key
        except ValueError:
            continue

def encrypt_3des(plaintext, key=None):
    if key is None:
        key = generate_valid_key()
    
    #generate a random vector
    iv = get_random_bytes(8)
    
    # convert the string to bytes and apply padding
    data = pad(plaintext.encode('utf-8'), DES3.block_size)
    
    #create the cipher object and encrypt
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    ciphertext = cipher.encrypt(data)
    
    return ciphertext, key, iv

def decrypt_3des(ciphertext, key, iv):
    #create the cipher object
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    
    #decrypt and remove padding
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext, DES3.block_size)
    
    return plaintext.decode('utf-8')

if __name__ == "__main__":
    # test the encryption and decryption
    with open("3des.txt", "r") as file:
        message = file.read()
    print("Original message:", message)
    
    #generate a valid key
    key = generate_valid_key()
    
    # encrypt
    encrypted_data, key, iv = encrypt_3des(message, key)
    print("Encrypted (hex):", encrypted_data.hex())
    print("Key (hex):", key.hex())
    print("IV (hex):", iv.hex())
    
    # decrypt
    decrypted_message = decrypt_3des(encrypted_data, key, iv)
    print("Decrypted message:", decrypted_message)
