import base64
from utils import base64_to_bin, dynamic_key_gen, ascii_to_bin, xor_bin, generate_bit_groups, bits_to_bytes
import numpy as np

def decript_image(image_path, output_path, key):
    # open the image
    with open(image_path, "rb") as image:
        # convert the image to base64
        base64_img = base64.b64encode(image.read()).decode('utf-8')
    
    # convert the base64 image to binary
    image_bits = base64_to_bin.base64_to_bin(base64_img).replace(" ", "")
    # get the binary representation of the key
    key_bin = ascii_to_bin.ascii_to_bin(key).replace(" ", "")
    # get the extended key
    extended_key_bits = dynamic_key_gen.complete_key(key_bin, len(image_bits))

    # separate the image and the key in groups of 8 bits
    separated_image_bits = generate_bit_groups.generate_bit_groups(image_bits)
    # separate the key in groups of 8 bits
    separated_key_bits = generate_bit_groups.generate_bit_groups(extended_key_bits)

    # get the xor of the image and the key
    decripted_image_bits = xor_bin.xor_bin(separated_image_bits, separated_key_bits)
    # convert the bits to bytes
    decripted_image_bytes = bits_to_bytes.bits_to_bytes(decripted_image_bits)

    # save the decripted image
    with open(output_path, 'wb') as f:
        f.write(decripted_image_bytes)

if __name__ == "__main__":
    image_path = "./imagen_xor.png"
    output_path = "./decripted_image.png"
    decript_image(image_path, output_path, "cifrados_2025")
