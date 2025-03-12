from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from PIL import Image
import numpy as np

def generate_key():
    return get_random_bytes(32)  # 32 bytes

def generate_iv():
    return get_random_bytes(16)  # 16 bytes

def encrypt_image_aes(image_path, mode='CBC'):
    img = Image.open(image_path)
    # convert to RGB if not already
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img_array = np.array(img)
    
    height, width, channels = img_array.shape
    
    # flatten image array
    flat_array = img_array.reshape(-1)
    img_bytes = flat_array.tobytes()
    # generate key
    key = generate_key()
    # pad data
    padded_data = pad(img_bytes, AES.block_size)
    
    if mode == 'CBC':
        # generate iv
        iv = generate_iv()
        # cypher with CBC mode
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted_data = cipher.encrypt(padded_data)
        encrypted_flat = np.frombuffer(encrypted_data, dtype=np.uint8)[:height*width*channels]
        encrypted_array = encrypted_flat.reshape((height, width, channels))
        
        return encrypted_array, key, iv
    
    elif mode == 'ECB':
        # cypher with ECB mode
        cipher = AES.new(key, AES.MODE_ECB)
        encrypted_data = cipher.encrypt(padded_data)
        encrypted_flat = np.frombuffer(encrypted_data, dtype=np.uint8)[:height*width*channels]
        encrypted_array = encrypted_flat.reshape((height, width, channels))
        
        return encrypted_array, key, None

def save_image(encrypted_array, output_path):
    # clip values to 0-255
    encrypted_array = np.clip(encrypted_array, 0, 255)
    # convert to uint8
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save(output_path)

if __name__ == "__main__":
    # cbc
    encrypted_cbc,key_cbc,iv_cbc = encrypt_image_aes("aes.png", mode='CBC')
    save_image(encrypted_cbc, "encrypted_cbc.png")
    
    # ecb
    encrypted_ecb,key_ecb, iv_ecb = encrypt_image_aes("aes.png", mode='ECB')
    save_image(encrypted_ecb, "encrypted_ecb.png")
