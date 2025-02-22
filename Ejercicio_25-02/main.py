from cypher import cypher, decypher

if __name__ == "__main__":
    plain_text = "Hello world!!!"
    nonce = "1234567890"
    cyphered = cypher(plain_text, nonce, False)
    print(f"cyphered text: {cyphered}")
    decyphered = decypher(cyphered, nonce, False)
    print(f"decyphered text: {decyphered}")
    
    