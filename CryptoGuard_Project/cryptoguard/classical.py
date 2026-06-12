import collections

class CaesarCipher:
    def __init__(self, shift_input):
        # Fig 4: Input Validation Interface for Caesar
        self.shift = self._validate_key(shift_input)

    def _validate_key(self, shift_input) -> int:
        try:
            shift = int(shift_input)
            return shift % 26
        except (ValueError, TypeError):
            print("\n[SECURITY ALERT] Invalid Caesar Key! Shift must be an integer.")
            print("[ACTION] Dropping malicious/malformed input.")
            raise ValueError("Caesar key must be an integer.")

    def encrypt(self, plaintext: str) -> str:
        result = []
        for char in plaintext:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                shifted = chr((ord(char) - start + self.shift) % 26 + start)
                result.append(shifted)
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        opposite_cipher = CaesarCipher(-self.shift)
        return opposite_cipher.encrypt(ciphertext)


class VigenereCipher:
    def __init__(self, key_input: str):
        # Fig 4: Input Validation Interface for Vigenère
        self.key = self._validate_key(key_input)

    def _validate_key(self, key_input: str) -> str:
        # Reject empty strings, numbers, or special symbols in the key
        if not key_input or not key_input.isalpha():
            print("\n[SECURITY ALERT] Invalid Vigenere Key! Key must contain LETTERS ONLY.")
            print(f"[REJECTED INPUT] '{key_input}' -> Boundary Security Guardrail Layer triggered.")
            raise ValueError("Vigenere key must contain letters only.")
        return key_input.lower()

    def encrypt(self, plaintext: str) -> str:
        result = []
        key_index = 0
        key_length = len(self.key)

        for char in plaintext:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                shift = ord(self.key[key_index % key_length]) - ord('a')
                shifted = chr((ord(char) - start + shift) % 26 + start)
                result.append(shifted)
                key_index += 1
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
                shifted = chr((ord(char) - start - shift + 26) % 26 + start)
                result.append(shifted)
                key_index += 1
            else:
                result.append(char)
        return "".join(result)


# --- Fig 5: Comprehensive Cipher Testing Interface ---
if __name__ == "__main__":
    print("\n" + "="*50)
    print("  BIT4138 ADVANCED CRYPTOGRAPHY - WEEK 2 LAB TEST  ")
    print("="*50)
    
    # Test 1: Successful Encryption Pipeline
    print("\n--- 1. CONFIRMED CORE DATA ENCRYPT LAYER ---")
    msg = "CryptoGuard Classical Encryption Pipeline 2026!"
    print(f"Plaintext: {msg}")
    
    v_cipher = VigenereCipher(key_input="GUARDKEY")
    ciphertext = v_cipher.encrypt(msg)
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted: {v_cipher.decrypt(ciphertext)}")
    
    # Frequency Distribution to analyze security weaknesses
    freq = collections.Counter(ciphertext.replace(" ", ""))
    print(f"Frequency Distribution: {dict(freq.most_common(5))}")

    # Test 2: Input Validation Intercept Simulation (Fig 4 Evidence)
    print("\n--- 2. TESTING BOUNDARY SECURITY GUARDRAIL LAYER ---")
    print("Simulating malicious/malformed key input injection...")
    try:
        malicious_cipher = VigenereCipher(key_input="MALICIOUS_INPUT_DROP_TABLES_123!")
    except ValueError:
        print("[SUCCESS] Input validation layer safely intercepted and dropped the threat.")
    print("="*50 + "\n")