from cypher import cypher, decypher
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 0:
        plain_text = "Hello world!!!"
        nonce = "1234567890"
    else:
        plain_text = args[0]
        nonce = args[1]
    cyphered = cypher(plain_text, nonce, False)
    print(f"cyphered text: {cyphered}")
    decyphered = decypher(cyphered, nonce, False)
    print(f"decyphered text: {decyphered}")
    
    