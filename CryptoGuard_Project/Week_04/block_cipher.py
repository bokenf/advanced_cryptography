from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

key = os.urandom(32)  # 256-bit key
iv = os.urandom(16)   # Initialization Vector

# Setting up ECB Mode (The insecure way)
ecb_cipher = Cipher(algorithms.AES(key), modes.ECB())

# Setting up CBC Mode (The secure way)
cbc_cipher = Cipher(algorithms.AES(key), modes.CBC(iv))

print("Cipher modes initialized.")
# Demonstrating the impact of the IV
plaintext = b"SecureData123456" # 16 bytes

# Encrypt twice with different IVs
iv1 = os.urandom(16)
iv2 = os.urandom(16)

cipher1 = Cipher(algorithms.AES(key), modes.CBC(iv1)).encryptor()
cipher2 = Cipher(algorithms.AES(key), modes.CBC(iv2)).encryptor()

ct1 = cipher1.update(plaintext) + cipher1.finalize()
ct2 = cipher2.update(plaintext) + cipher2.finalize()

print(f"Ciphertext 1 (IV 1): {ct1.hex()}")
print(f"Ciphertext 2 (IV 2): {ct2.hex()}")
from cryptography.hazmat.primitives import padding

# Data that is NOT a multiple of 16 bytes (13 bytes)
data = b"Hello World!!" 
padder = padding.PKCS7(128).padder() # 128-bit block size

# Add padding
padded_data = padder.update(data) + padder.finalize()

print(f"Original: {data}")
print(f"Padded:   {padded_data}")
print(f"Length:   {len(padded_data)} bytes")
# Comparison of ECB vs CBC
message = b"SECRETSECRETSEC" * 2 # Repeated pattern
padder = padding.PKCS7(128).padder()
padded_msg = padder.update(message) + padder.finalize()

# ECB: The insecure mode
ecb_enc = Cipher(algorithms.AES(key), modes.ECB()).encryptor()
ct_ecb = ecb_enc.update(padded_msg) + ecb_enc.finalize()

# CBC: The secure mode
cbc_enc = Cipher(algorithms.AES(key), modes.CBC(iv)).encryptor()
ct_cbc = cbc_enc.update(padded_msg) + cbc_enc.finalize()

print(f"ECB Ciphertext: {ct_ecb.hex()}")
print(f"CBC Ciphertext: {ct_cbc.hex()}")
# Decrypting the CBC ciphertext
decryptor = Cipher(algorithms.AES(key), modes.CBC(iv)).decryptor()
decrypted_padded = decryptor.update(ct_cbc) + decryptor.finalize()

# Unpadding
unpadder = padding.PKCS7(128).unpadder()
decrypted_data = unpadder.update(decrypted_padded) + unpadder.finalize()

print(f"Original Data:  {message}")
print(f"Decrypted Data: {decrypted_data}")