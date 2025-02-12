from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def merge_images_xor(image1_path, image2_path, output_path):
    #open images
    main_image = Image.open(image1_path)
    key_image = Image.open(image2_path)
    
    #make sure the images are in the same format
    main_image = main_image.convert('RGB')
    key_image = key_image.convert('RGB')
    #resize the key image to the size of the main image
    key_image = key_image.resize(main_image.size)
    
    #convert the images to numpy arrays
    main_array = np.array(main_image)
    key_array = np.array(key_image)
    
    #apply the xor operation
    merged_array = np.bitwise_xor(main_array, key_array)
    #convert the result to an image
    merged_image = Image.fromarray(merged_array.astype(np.uint8))
    #save the result
    merged_image.save(output_path)
    
    return main_image, key_image, merged_image

if __name__ == "__main__":
    main_image_path = "images/img1.jpg"
    key_image_path = "images/img2.jpg"
    output_path = "images/merged_image.png"
    
    #merge images
    img1, img2, result = merge_images_xor(main_image_path, key_image_path, output_path)
    
    #show images
    plt.figure(figsize=(10, 10))
    plt.subplot(131)
    plt.imshow(img1)
    plt.title("Main Image")
    plt.axis('off')

    plt.subplot(132)
    plt.imshow(img2)
    plt.title("Key Image")
    plt.axis('off')

    plt.subplot(133)
    plt.imshow(result)
    plt.title("Merged Image")
    plt.axis('off')

    plt.show()