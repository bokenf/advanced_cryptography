# Figure 1: SPN vs Feistel Architecture Comparison
def get_feistel_structure():
    return "Feistel: [Left Half] <---> [Right Half] (Swap & XOR)"

def get_spn_structure():
    return "SPN: [Entire Block] ---> (Sub) ---> (Perm) ---> (Mix)"

print("---Structural Comparison ---")
print("1. " + get_feistel_structure())
print("2. " + get_spn_structure())