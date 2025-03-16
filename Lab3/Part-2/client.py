import socket
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

# create a tcp socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
server_address = ('localhost', 9876)
print('Connecting to {}:{}'.format(*server_address))
sock.connect(server_address)

def encrypt_AES_CBC(message):
    # generate a random key and iv
    key = get_random_bytes(16)
    iv = get_random_bytes(16)

    # encrypt the message
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(message, AES.block_size)
    ciphertext = cipher.encrypt(padded_data)

    return ciphertext

try:
    # read data from file
    with open('./data.txt', 'r') as file:
        message = file.read().encode('utf-8')

    # encrypt the message
    encrypted_message = encrypt_AES_CBC(message)

    # send data
    print('Sending: {!r}'.format(encrypted_message))
    sock.sendall(encrypted_message)

finally:
    print('Closing socket')
    sock.close() 