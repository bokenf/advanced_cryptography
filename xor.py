# Figure 1: XOR-Based Cryptanalysis
# Demonstrate algebraic weakness in simple systems
plaintext = 12
key = 5

# Encryption: C = P XOR K
ciphertext = plaintext ^ key

# Cryptanalysis: Recovering key via K = C XOR P
recovered = ciphertext ^ plaintext

print("--- XOR-Based Analysis ---")
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Recovered Key: {recovered}")