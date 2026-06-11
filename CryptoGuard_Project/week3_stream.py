import os

def generate_prng_keystream(length: int) -> bytes:
    """
    Simulating a secure PRNG stream layer.
    In production, this relies on cryptographically secure entropy sources.
    """
    return os.urandom(length)

def stream_encrypt_decrypt(data: str, keystream: bytes) -> tuple:
    # Convert input string text asset into raw bytes
    input_bytes = data.encode('utf-8')
    
    # Core Bitwise XOR Stream Execution Engine Logic Layer
    processed_bytes = bytes([b ^ k for b, k in zip(input_bytes, keystream)])
    
    # Hexadecimal Encoding Representation Layer for safe data rendering
    hex_output = processed_bytes.hex().upper()
    return processed_bytes, hex_output

if __name__ == "__main__":
    print("--- Running CryptoGuard Stream Cipher Pipeline ---")
    secret_payload = "CONFIRMED INTEL MISSION ACCOMPLISHED"
    payload_length = len(secret_payload.encode('utf-8'))
    
    # 1. Generate Keystream Asset Engine
    simulated_keystream = generate_prng_keystream(payload_length)
    print(f"Generated PRNG Keystream (Hex Shorthand Form): {simulated_keystream.hex().upper()[:30]}...")
    
    # 2. Run Encryption Processing Stream
    cipher_bytes, cipher_hex = stream_encrypt_decrypt(secret_payload, simulated_keystream)
    print(f"\nPlaintext Data Input:    {secret_payload}")
    print(f"Encrypted Hex Network Asset: {cipher_hex}")
    
    # 3. Run Decryption Processing Stream (XOR Symmetric Inversion Property)
    decrypted_bytes, _ = stream_encrypt_decrypt(cipher_bytes.decode('latin1'), simulated_keystream)
    recovered_text = decrypted_bytes.decode('utf-8', errors='ignore')
    print(f"Symmetric Recovered Output:  {recovered_text}")
