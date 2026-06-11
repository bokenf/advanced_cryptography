class RC4:
    def __init__(self, key: bytes):
        self.key = key

    def _ksa(self) -> list:
        """Key Scheduling Algorithm (KSA) - Initializes the permutation vector S."""
        S = list(range(256))
        j = 0
        key_length = len(self.key)
        
        for i in range(256):
            j = (j + S[i] + self.key[i % key_length]) % 256
            S[i], S[j] = S[j], S[i]  # Swap values
        return S

    def _prga(self, S: list, data_length: int) -> bytes:
        """Pseudo-Random Generation Algorithm (PRGA) - Generates the keystream."""
        i = 0
        j = 0
        keystream = []
        
        for _ in range(data_length):
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]  # Swap values
            
            K = S[(S[i] + S[j]) % 256]
            keystream.append(K)
        return bytes(keystream)

    def encrypt(self, plaintext: bytes) -> bytes:
        """Encrypts plaintext by XORing it with the generated keystream."""
        S = self._ksa()
        keystream = self._prga(S, len(plaintext))
        return bytes(p ^ k for p, k in zip(plaintext, keystream))

    def decrypt(self, ciphertext: bytes) -> bytes:
        """RC4 decryption is identical to encryption due to the nature of XOR operations."""
        return self.encrypt(ciphertext)


if __name__ == "__main__":
    print("--- Testing Week 2 Stream Cipher (RC4) ---")
    secret_key = b"CryptoGuardKey2026"
    cipher = RC4(secret_key)
    
    message = b"Testing our official Week 2 Stream Module!"
    encrypted = cipher.encrypt(message)
    print(f"RC4 Encrypted (Hex): {encrypted.hex()}")
    print(f"RC4 Decrypted: {cipher.decrypt(encrypted).decode()}")