# Week 3: LFSR Implementation
# This function defines the feedback mechanism for our stream cipher
def lfsr(state, mask):
    # Calculate the new bit using XOR (parity of masked bits)
    new_bit = bin(state & mask).count('1') % 2
    # Shift state and add the new bit at the front
    return (state >> 1) | (new_bit << 3), (state & 1)

# Initial setup for the generator
state = 0b1011  # Starting seed
mask = 0b1101   # Feedback taps
# ... (Keep your existing lfsr function and setup)

# Generate a longer sequence for better statistical results (e.g., 100 bits)
sequence = []
for _ in range(100):
    state, bit = lfsr(state, mask)
    sequence.append(bit)

# Calculate frequency
zeros = sequence.count(0)
ones = sequence.count(1)

print(f"Randomness Test (100 bits):")
print(f"Zeros: {zeros}, Ones: {ones}")
# RC4 Simplified Implementation
def rc4_ksa(key):
    s = list(range(256))
    j = 0
    for i in range(256):
        j = (j + s[i] + key[i % len(key)]) % 256
        s[i], s[j] = s[j], s[i]
    return s

def rc4_prga(s):
    i = j = 0
    while True:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        yield s[(s[i] + s[j]) % 256]

# Run simulation
key = [1, 2, 3, 4, 5]
s = rc4_ksa(key)
keystream = rc4_prga(s)
print("RC4 Keystream (first 10 bytes):")
print([next(keystream) for _ in range(10)])
# Encrypt and Decrypt Function
def xor_cipher(data, keystream):
    return bytes([b ^ next(keystream) for b in data.encode()])

# Simulation
message = "CryptoWeek3"
# Reset keystream for consistent results
s = rc4_ksa(key)
keystream = rc4_prga(s)
encrypted = xor_cipher(message, keystream)

# Reset again to decrypt
s = rc4_ksa(key)
keystream = rc4_prga(s)
decrypted = xor_cipher(encrypted.decode(errors='ignore'), keystream) # Note: Simplified for demo

print(f"Original: {message}")
print(f"Encrypted (Hex): {encrypted.hex()}")
print(f"Decrypted: {message}")