import unittest
from cypher import cypher, decypher

class TestCypher(unittest.TestCase):
    def test_cypher(self):
        plain_text = "Hello world!!!"
        keystream = "1234567890"
        cyphered = cypher(plain_text, keystream, False)
        decyphered = decypher(cyphered, keystream, False)
        self.assertEqual(decyphered, plain_text)

if __name__ == "__main__":
    unittest.main()
