from utils import base64_to_bin, bin_to_ascii

def base64_to_ascii(base64):
    return bin_to_ascii.bin_to_ascii(base64_to_bin.base64_to_bin(base64))

if __name__ == "__main__":
    # Example 1
    arg = "SGVsbG8hIQ=="
    res = base64_to_ascii(arg)
    print('The ascii code of the base64 representation "'+ arg + '" is', res)

    # Example 2
    arg = "SGVsbG8gd29ybGQ="
    res = base64_to_ascii(arg)
    print('The ascii code of the base64 representation "'+ arg + '" is', res)