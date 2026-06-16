from cryptography.fernet import Fernet

# Generate a key and save it
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Test encryption
message = b"Cryptography Week 1 Setup Successful"
cipher_text = cipher_suite.encrypt(message)
plain_text = cipher_suite.decrypt(cipher_text)

print(f"Original: {message}")
print(f"Encrypted: {cipher_text}")
print(f"Decrypted: {plain_text.decode()}")