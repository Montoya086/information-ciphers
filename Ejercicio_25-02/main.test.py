import unittest
from cypher import cypher, decypher

class TestCypher(unittest.TestCase):
    def test_cypher(self):
        plain_text = "Hello world!!!"
        nonce = "1234567890"
        cyphered = cypher(plain_text, nonce, False)
        decyphered = decypher(cyphered, nonce, False)
        self.assertEqual(decyphered, plain_text)

if __name__ == "__main__":
    unittest.main()
