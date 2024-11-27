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

def read_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

def write_file(file_path, data):
    with open(file_path, 'wb') as file:
        file.write(data)

def encrypt_file(input_file_path, output_file_path, key, iv=None):
    if iv is None:
        iv = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = read_file(input_file_path)
    padded_plaintext = pad(plaintext)
    ciphertext = cipher.encrypt(padded_plaintext)
    write_file(output_file_path, iv + ciphertext)

def decrypt_file(input_file_path, output_file_path, key, iv=None):
    if iv is None:
        iv = read_file(input_file_path)[:16]
        ciphertext = read_file(input_file_path)[16:]
    else:
        ciphertext = read_file(input_file_path)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext)
    write_file(output_file_path, plaintext)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Encrypt or decrypt a file using AES.")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("output_file", help="Path to the output file")
    parser.add_argument("--key_file", help="Path to the file containing the AES key")
    parser.add_argument("--iv_file", help="Path to the file containing the IV")
    parser.add_argument("--encrypt", action="store_true", help="Encrypt the file")
    parser.add_argument("--decrypt", action="store_true", help="Decrypt the file")

    args = parser.parse_args()

    if args.key_file:
        key = read_file(args.key_file)
    else:
        key = get_random_bytes(32)

    if args.iv_file:
        iv = read_file(args.iv_file)
    else:
        iv = None

    if args.encrypt:
        encrypt_file(args.input_file, args.output_file, key, iv)
        print(f"File encrypted and saved to {args.output_file}")
    elif args.decrypt:
        decrypt_file(args.input_file, args.output_file, key, iv)
        print(f"File decrypted and saved to {args.output_file}")
    else:
        print("Please specify either --encrypt or --decrypt.")
