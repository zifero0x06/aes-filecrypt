from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

# Fixed key and IV
FIXED_KEY = b'fixedkey1234567890123456'  # 256-bit key (32 bytes)
FIXED_IV = b'fixediv12345678'  # 128-bit IV (16 bytes)

def pad(data):
    # AES requires the data to be a multiple of 16 bytes
    padding_length = 16 - (len(data) % 16)
    return data + bytes([padding_length] * padding_length)

def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]

def read_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

def write_file(file_path, data):
    with open(file_path, 'wb') as file:
        file.write(data)

def encrypt_file(input_file_path, output_file_path, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = read_file(input_file_path)
    padded_plaintext = pad(plaintext)
    ciphertext = cipher.encrypt(padded_plaintext)
    write_file(output_file_path, iv + ciphertext)

def decrypt_file(input_file_path, output_file_path, key, iv):
    ciphertext = read_file(input_file_path)[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext)
    write_file(output_file_path, plaintext)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Encrypt or decrypt a file using AES.")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("output_file", help="Path to the output file")
    parser.add_argument("--encrypt", action="store_true", help="Encrypt the file")
    parser.add_argument("--decrypt", action="store_true", help="Decrypt the file")

    args = parser.parse_args()

    if args.encrypt:
        encrypt_file(args.input_file, args.output_file, FIXED_KEY, FIXED_IV)
        print(f"File encrypted and saved to {args.output_file}")
    elif args.decrypt:
        decrypt_file(args.input_file, args.output_file, FIXED_KEY, FIXED_IV)
        print(f"File decrypted and saved to {args.output_file}")
    else:
        print("Please specify either --encrypt or --decrypt.")
