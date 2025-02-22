import os
import random
import string

def generate_key(length=16, seed=None):
    if seed is None:
        seed = os.urandom(length)
    # set the seed for the random number generator
    random.seed(seed)
    # generate a random number key using all the characters
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return key

if __name__ == "__main__":
    print("-"*50)
    print("Example 1:")
    length = 16
    seed = "1234567890"
    print(f"length: {length}")
    print(f"seed: {seed}")
    print(f"key: {generate_key(length, seed)}")
    print("-"*50+"\n")

    print("-"*50)
    print("Example 2:")
    length = 32
    seed = "asdf1234"
    print(f"length: {length}")
    print(f"seed: {seed}")
    print(f"key: {generate_key(length, seed)}")
    print("-"*50+"\n")