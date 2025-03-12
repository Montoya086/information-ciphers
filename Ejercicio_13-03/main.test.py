import unittest
from des import encrypt_des, decrypt_des, get_random_bytes
from des3 import encrypt_3des, decrypt_3des

class TestDes(unittest.TestCase):
    def test_encrypt_des(self):
        plaintext = "Hello world!!!"
        key = get_random_bytes(8)
        encrypted, key = encrypt_des(plaintext, key)
        decrypted = decrypt_des(encrypted, key)
        self.assertEqual(decrypted, plaintext)

class TestDes3(unittest.TestCase):
    def test_encrypt_3des(self):
        plaintext = "Hello world!!!"
        key = get_random_bytes(24)
        encrypted, key, iv = encrypt_3des(plaintext, key)
        decrypted = decrypt_3des(encrypted, key, iv)
        self.assertEqual(decrypted, plaintext)

if __name__ == "__main__":
    unittest.main()
