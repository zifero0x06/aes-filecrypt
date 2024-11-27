from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

def pad(data):
    # AES requires the data to be a multiple of 16 bytes
    padding_length = 16 - (len(data) % 16)
    return data + bytes([padding_length] * padding_length)

def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]

def encrypt_file(input_file_path, output_file_path, key):
    # Generate a random IV (Initialization Vector)
    iv = get_random_bytes(16)

    # Create AES cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Read the input file
    with open(input_file_path, 'rb') as input_file:
        plaintext = input_file.read()

    # Pad the plaintext to be a multiple of 16 bytes
    padded_plaintext = pad(plaintext)

    # Encrypt the padded plaintext
    ciphertext = cipher.encrypt(padded_plaintext)

    # Write the IV and ciphertext to the output file
    with open(output_file_path, 'wb') as output_file:
        output_file.write(iv)
        output_file.write(ciphertext)

def decrypt_file(input_file_path, output_file_path, key):
    # Read the input file
    with open(input_file_path, 'rb') as input_file:
        iv = input_file.read(16)
        ciphertext = input_file.read()

    # Create AES cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the ciphertext
    padded_plaintext = cipher.decrypt(ciphertext)

    # Unpad the plaintext
    plaintext = unpad(padded_plaintext)

    # Write the plaintext to the output file
    with open(output_file_path, 'wb') as output_file:
        output_file.write(plaintext)

# Example usage
if __name__ == "__main__":
    # Generate a random 256-bit key
    key = get_random_bytes(32)

    # Paths to the input and output files
    input_file_path = 'input.txt'
    encrypted_file_path = 'encrypted.bin'
    decrypted_file_path = 'decrypted.txt'

    # Encrypt the file
    encrypt_file(input_file_path, encrypted_file_path, key)
    print(f"File encrypted and saved to {encrypted_file_path}")

    # Decrypt the file
    decrypt_file(encrypted_file_path, decrypted_file_path, key)
    print(f"File decrypted and saved to {decrypted_file_path}")
