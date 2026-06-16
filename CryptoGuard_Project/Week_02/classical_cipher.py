# 1. DEFINE FUNCTIONS FIRST
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def vigenere_encrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
            key_index += 1
        else:
            result += char
    return result

# 2. DEFINE DATA SECOND
message = "Hello World"
shift_key = 3
key = "SECRET"

# 3. EXECUTE ACTIONS LAST
print(f"Original: {message}")
print(f"Caesar Encrypted: {caesar_encrypt(message, shift_key)}")
print(f"Vigenere Encrypted: {vigenere_encrypt(message, key)}")

# --- USER INPUT VALIDATION INTERFACE ---
print("\n--- Cipher Interface ---")
user_text = input("Enter text to encrypt: ")
if not user_text:
    print("Error: Text cannot be empty!")
else:
    user_key = input("Enter Vigenere key (letters only): ")
    if not user_key.isalpha():
        print("Error: Key must contain letters only!")
    else:
        print(f"Result: {vigenere_encrypt(user_text, user_key)}")