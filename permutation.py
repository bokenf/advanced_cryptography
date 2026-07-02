# Figure 3: Bit-wise Permutation Logic
def apply_permutation(data):
    # Mapping based on Week 6 Class Demonstration 2
    # Original: ABCD (Indices 0123) -> Permuted: CDAB (Indices 2301)
    permuted = data[2] + data[3] + data[0] + data[1]
    return permuted

print("--- Bit-wise Permutation ---")
original = "ABCD"
result = apply_permutation(original)
print(f"Original: {original}")
print(f"Permuted: {result}")