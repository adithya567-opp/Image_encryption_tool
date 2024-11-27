from PIL import Image
import numpy as np

def encrypt_image(image_path,key):
    try:
        # Open the image
        image_path = r"C:\Users\kvadi\Documents\python\butterfly.jpg"
        img = Image.open(image_path)
        # Convert the image to a NumPy array
        img_array = np.array(img)
        # Ensure the key has the same shape as img_array
        key = np.resize(key, img_array.shape)
        # Encrypt each pixel with XOR with the key
        encrypted_array = np.bitwise_xor(img_array, key)
        # Convert the encrypted array back to an image
        encrypted_img = Image.fromarray(encrypted_array)
        # Save the encrypted image
        encrypted_img_path = r"C:\Users\kvadi\Documents\python\encrypted_img.png"
        encrypted_img.save(encrypted_img_path)
        print("Image encrypted successfully.")
        return encrypted_img_path
    except Exception as e:
        print(f"Error during encryption: {e}")
        return None


def decrypt_image(encrypted_img_path,key):
    try:
        print(f"Decrypting image from: {encrypted_img_path}")
        # Open the encrypted image
        encrypted_img = Image.open(encrypted_img_path)
        # Convert the image to a NumPy array
        encrypted_array = np.array(encrypted_img)
        # Ensure the key has the same shape as img_array
        key = np.resize(key, encrypted_array.shape)
        # Decrypt each pixel with XOR with the key
        decrypted_array = np.bitwise_xor(encrypted_array, key)
        # Convert the decrypted array back to an image
        decrypted_img = Image.fromarray(decrypted_array)
        # Save the decrypted image
        output_path = r"C:\Users\kvadi\Documents\python\decrypted_img.png"
        decrypted_img.save(output_path)
        print(f"Decrypted image saved as {output_path}.")
    except Exception as e:
        print(f"Error during decryption: {e}")

def main():
    print("Image Encryption and Decryption using Pixel Manipulation")
    try:
        # Get the image path
        image_path = input("Enter the path to the image file: ")
        # Generate a random key (you can use any integer as the key)
        key = np.random.randint(0, 256, size=(3,), dtype=np.uint8)
        print(f"Generated key: {key}")
        # Encrypt the image
        encrypted_img_path = encrypt_image(image_path, key)
        if encrypted_img_path:
            # Decrypt the image
            decrypt_image(encrypted_img_path, key)
    except Exception as e:
        print(f"Error in the main function: {e}")
    

if __name__ == "__main__":
    main()