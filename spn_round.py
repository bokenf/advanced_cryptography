# Figure 4: Full SPN Round Logic
def s_box_layer(val):
    # Mapping: 0->14, 1->4, 2->13, 3->1 (Simplified 4-bit S-Box)
    s_box = {0: 14, 1: 4, 2: 13, 3: 1}
    return s_box.get(val, 0)

def apply_spn_round(plaintext, key):
    # 1. Key Mixing (XOR)
    mixed = plaintext ^ key
    # 2. Substitution (S-Box)
    substituted = s_box_layer(mixed)
    # 3. Permutation (Bit-wise shift example)
    # Rotating bits: (substituted >> 1) | ((substituted & 1) << 3)
    permuted = ((substituted >> 1) | ((substituted & 1) << 3)) & 0xF
    return permuted

print("--- Figure 4: Full SPN Round ---")
p = 2
k = 3
result = apply_spn_round(p, k)
print(f"Input Plaintext: {p} | Round Key: {k}")
print(f"Final SPN Round Output: {result}")