def dynamic_key_gen(key, size):
    # get the size of the key
    key_size = len(key)
    # calculate the number of keys to concatenate
    number_of_keys = size // key_size
    # calculate the number of characters left
    leftover = size % key_size
    # return the generated key with the number of keys and the leftover characters
    return key * number_of_keys + key[:leftover]

if __name__ == "__main__":
    key = "key"
    size = 10
    print(dynamic_key_gen(key, size))