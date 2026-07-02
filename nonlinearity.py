# Figure 6: Non-Linearity Analysis
def s_box(val):
    # S-Box mapping
    mapping = {0: 14, 1: 4, 2: 13, 3: 1}
    return mapping.get(val, 0)

# Testing Linearity Property: f(a ^ b) == f(a) ^ f(b)?
a, b = 1, 2
lhs = s_box(a ^ b)       # f(1 ^ 2) = f(3) = 1
rhs = s_box(a) ^ s_box(b) # f(1) ^ f(2) = 4 ^ 13 = 9

print("--- Figure 6: Non-Linearity Analysis ---")
print(f"LHS (f(a ^ b)): {lhs}")
print(f"RHS (f(a) ^ f(b)): {rhs}")
print(f"Is Linear? {lhs == rhs}")