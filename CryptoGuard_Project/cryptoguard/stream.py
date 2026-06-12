import collections
import math

class LFSR:
    """Implements a Linear Feedback Shift Register for pseudorandom bit generation."""
    def __init__(self, state: int, taps: list):
        self.state = state & 0xF  # 4-bit state registers (e.g., 0b1011)
        self.taps = taps          # Tap positions for feedback (e.g., [4, 3] for primitive polynomial)

    def step(self) -> int:
        """Executes one clock cycle shift and returns the output bit."""
        # Calculate feedback bit by XORing the tapped bits
        feedback = 0
        for tap in self.taps:
            # Extract the bit at the tap position (1-indexed from right)
            feedback ^= (self.state >> (tap - 1)) & 1
            
        output_bit = self.state & 1  # LSB is the output bit
        
        # Shift state right and place the feedback bit at the MSB (4-bit system)
        self.state = ((self.state >> 1) | (feedback << 3)) & 0xF
        return output_bit

    def generate_sequence(self, length: int) -> list:
        """Generates a pseudorandom stream of bits of a specified length."""
        return [self.step() for _ in range(length)]


class RC4:
    """Implements the standard RC4 Stream Cipher Engine."""
    def __init__(self, key: bytes):
        self.key = key

    def _ksa(self) -> list:
        S = list(range(256))
        j = 0
        key_length = len(self.key)
        for i in range(256):
            j = (j + S[i] + self.key[i % key_length]) % 256
            S[i], S[j] = S[j], S[i]
        return S

    def _prga(self, S: list, data_length: int) -> bytes:
        i = 0
        j = 0
        keystream = []
        for _ in range(data_length):
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            K = S[(S[i] + S[j]) % 256]
            keystream.append(K)
        return bytes(keystream)

    def encrypt(self, plaintext: bytes) -> bytes:
        S = self._ksa()
        keystream = self._prga(S, len(plaintext))
        return bytes(p ^ k for p, k in zip(plaintext, keystream))

    def decrypt(self, ciphertext: bytes) -> bytes:
        return self.encrypt(ciphertext)


# --- Week 3: Run-Time Testing & Statistical Analysis Simulation ---
if __name__ == "__main__":
    print("\n" + "="*55)
    print("  BIT4138 ADVANCED CRYPTOGRAPHY - WEEK 3 LAB TEST  ")
    print("="*55)

    # 1. LFSR Bit Generation (Fig 1 & 2 Evidence)
    print("\n--- 1. LINEAR FEEDBACK SHIFT REGISTER (LFSR) SEQUENCE ---")
    initial_seed = 0b1001
    feedback_taps = [4, 3]  # x^4 + x^3 + 1 primitive polynomial config
    lfsr = LFSR(state=initial_seed, taps=feedback_taps)
    
    bit_stream = lfsr.generate_sequence(20)
    print(f"LFSR Initial Seed:   {bin(initial_seed)}")
    print(f"Generated Bitstream: {bit_stream}")

    # 2. Statistical Randomness Testing (Fig 3 Evidence)
    print("\n--- 2. STATISTICAL RANDOMNESS ANALYSIS ---")
    bit_counts = collections.Counter(bit_stream)
    ones = bit_counts.get(1, 0)
    zeros = bit_counts.get(0, 0)
    print(f"Frequency Count -> Ones (1s): {ones}, Zeros (0s): {zeros}")
    
    # Frequency test (Monobit test approximation)
    proportion = ones / len(bit_stream)
    print(f"Monobit Density Balance: {proportion:.2f} (Ideal: 0.50)")

    # 3. RC4 Simulation & Performance Execution (Fig 4 & 5 Evidence)
    print("\n--- 3. RC4 STREAM CIPHER SIMULATION ---")
    secret_key = b"StreamGuardSecure2026"
    rc4_engine = RC4(secret_key)
    
    plaintext_msg = b"Confidential Advanced Cryptography Data Payload Stream"
    print(f"Plaintext bytes: {plaintext_msg}")
    
    ciphertext = rc4_engine.encrypt(plaintext_msg)
    print(f"Ciphertext (Hex): {ciphertext.hex().upper()}")
    
    decrypted = rc4_engine.decrypt(ciphertext)
    print(f"Decrypted Result: {decrypted.decode()}")
    print("="*55 + "\n")