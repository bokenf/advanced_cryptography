# Figure 5: Avalanche Effect
def s_box_layer(val):
    s_box = {0: 14, 1: 4, 2: 13, 3: 1, 4: 0, 5: 15, 6: 12, 7: 8, 8: 3, 9: 10, 10: 6, 11: 2, 12: 5, 13: 9, 14: 0, 15: 7}
    return s_box.get(val % 16, 0)

def apply_spn_round(p, k):
    mixed = p ^ k
    sub = s_box_layer(mixed)
    return ((sub >> 1) | ((sub & 1) << 3)) & 0xF

print("--- Figure 5: Avalanche Effect ---")
p1, p2 = 2, 3  # Binary 0010 and 0011 (differ by 1 bit)
k = 5
out1 = apply_spn_round(p1, k)
out2 = apply_spn_round(p2, k)

print(f"Input 1: {bin(p1)} -> Output 1: {bin(out1)}")
print(f"Input 2: {bin(p2)} -> Output 2: {bin(out2)}")
print("Observation: A single bit change in input leads to different outputs.")