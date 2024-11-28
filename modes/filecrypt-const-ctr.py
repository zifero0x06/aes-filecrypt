import sys
from Crypto.Cipher import AES
from Crypto.Util import Counter
import base64

# Fixed key and nonce
FIXED_KEY = b'fixedkey1234567890123456'  # 256-bit key (32 bytes)
FIXED_NONCE = b'fixednonce123456'  # 96-bit nonce (12 bytes)

def encrypt(plaintext):
    ctr = Counter.new(128, initial_value=int.from_bytes(FIXED_NONCE, byteorder='big'))
    cipher = AES.new(FIXED_KEY, AES.MODE_CTR, counter=ctr)
    ciphertext = cipher.encrypt(plaintext)
    return base64.b64encode(ciphertext)

def decrypt(ciphertext):
    ciphertext = base64.b64decode(ciphertext)
    ctr = Counter.new(128, initial_value=int.from_bytes(FIXED_NONCE, byteorder='big'))
    cipher = AES.new(FIXED_KEY, AES.MODE_CTR, counter=ctr)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def main():
    if len(sys.argv) < 4:
        print("Usage: python aes_ctr_file.py <encrypt|decrypt> <input_file> <output_file>")
        sys.exit(1)

    action = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    try:
        with open(input_file, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        print(f"File {input_file} not found.")
        sys.exit(1)

    if action == "encrypt":
        encrypted_data = encrypt(data)
        with open(output_file, 'wb') as f:
            f.write(encrypted_data)
        print(f"Encrypted data written to {output_file}")
    elif action == "decrypt":
        decrypted_data = decrypt(data)
        with open(output_file, 'wb') as f:
            f.write(decrypted_data)
        print(f"Decrypted data written to {output_file}")
    else:
        print("Invalid action. Use 'encrypt' or 'decrypt'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
