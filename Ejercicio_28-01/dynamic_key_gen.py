import random

def dynamic_key_gen(size):
    # generate a random ascii key of the given size
    key = ""
    for _ in range(size):
        key += chr(random.randint(0, 255))
    return key

def complete_key(key, size):
    # get the size of the key
    key_size = len(key)
    # calculate the number of keys to concatenate
    number_of_keys = size // key_size
    # calculate the number of characters left
    leftover = size % key_size
    # return the generated key with the number of keys and the leftover characters
    return key * number_of_keys + key[:leftover]

if __name__ == "__main__":
    size = 10
    print(dynamic_key_gen(size))


#dyamic: metes una longitud y te devuelve una clave de esa longitud y ajustas la palabra para que tenga esa longitud
#static: metes una clave y recortas o alargas la clave para que tenga la longitud de la palabra