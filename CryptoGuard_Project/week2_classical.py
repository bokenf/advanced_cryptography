import collections

def validate_and_encrypt(text: str, key: str):
    """
    CryptoGuard Input Filtering Layer:
    Ensures only alphabetic characters and spaces pass through.
    Blocks special symbols or numerical strings to protect system logic.
    """
    if not text.replace(" ", "").isalpha():
        print("Security Alert: Invalid input characters blocked by CryptoGuard guardrail!")
        return
        
    text, key = text.upper(), key.upper()
    cipher = []
    
    # Polyalphabetic Multi-Character Character Shifting Loop
    for i, char in enumerate(text):
        if char == " ":
            cipher.append(" ")
            continue
        # Derive structural shift factor using keyword index position cycling
        shift = ord(key[i % len(key)]) - ord('A')
        cipher.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        
    ciphertext = "".join(cipher)
    print(f"Plaintext Input:  {text}")
    print(f"Ciphertext Asset: {ciphertext}")
    
    # Frequency Distribution Analysis (Cryptanalysis Simulation Testing)
    print(f"Top Character Frequency Distribution: {collections.Counter(ciphertext.replace(' ', '')).most_common(1)}")

# --- Local Script Execution ---
if __name__ == "__main__":
    print("--- Running CryptoGuard Classical Encryption Pipeline ---")
    validate_and_encrypt("CONFIRMED CORE DATA ENCRYPT LAYER", "GUARDKEY")
    
    print("\n--- Testing Boundary Security Guardrail Layer ---")
    validate_and_encrypt("MALICIOUS_INPUT_DROP_TABLES_123!", "GUARDKEY")
