class CaesarCipher:
    def __init__(self, shift: int):
        self.shift = shift % 26

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                # Apply shift using modular arithmetic (26 letters in the alphabet)
                shifted = chr((ord(char) - start + self.shift) % 26 + start)
                result.append(shifted)
            else:
                result.append(char)  # Keep punctuation and spaces as-is
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        # Decryption is just shifting in the opposite direction
        opposite_cipher = CaesarCipher(-self.shift)
        return opposite_cipher.encrypt(ciphertext)


class VigenereCipher:
    def __init__(self, key: str):
        self.key = key.lower()

    def encrypt(self, plaintext: str) -> str:
        result = []
        key_index = 0
        key_length = len(self.key)

        for char in plaintext:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                # Determine the shift value from the current key character
                shift = ord(self.key[key_index % key_length]) - ord('a')
                
                shifted = chr((ord(char) - start + shift) % 26 + start)
                result.append(shifted)
                key_index += 1  # Only move key index if we processed an actual letter
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        key_index = 0
        key_length = len(self.key)

        for char in ciphertext:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                shift = ord(self.key[key_index % key_length]) - ord('a')
                
                # Subtract the shift for decryption
                shifted = chr((ord(char) - start - shift + 26) % 26 + start)
                result.append(shifted)
                key_index += 1
            else:
                result.append(char)
        return "".join(result)


# Quick Test execution
if __name__ == "__main__":
    print("--- Testing Week 1 Classical Ciphers ---")
    message = "CryptoGuard Project, Week 1!"
    
    # Test Caesar
    caesar = CaesarCipher(shift=3)
    caesar_encrypted = caesar.encrypt(message)
    print(f"Caesar Encrypted: {caesar_encrypted}")
    print(f"Caesar Decrypted: {caesar.decrypt(caesar_encrypted)}\n")
    
    # Test Vigenere
    vigenere = VigenereCipher(key="KEY")
    vigenere_encrypted = vigenere.encrypt(message)
    print(f"Vigenere Encrypted: {vigenere_encrypted}")
    print(f"Vigenere Decrypted: {vigenere.decrypt(vigenere_encrypted)}")