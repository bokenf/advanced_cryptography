# Figure 7: Difference Distribution Table (DDT)
def generate_ddt(s_box):
    n = len(s_box)
    ddt = [[0 for _ in range(n)] for _ in range(n)]
    for delta_in in range(n):
        for x in range(n):
            delta_out = s_box[x] ^ s_box[x ^ delta_in]
            ddt[delta_in][delta_out] += 1
    return ddt

# Your S-Box from earlier
s_box = [0xE, 0x4, 0xD, 0x1, 0x2, 0xF, 0xB, 0x8, 0x3, 0xA, 0x6, 0xC, 0x5, 0x9, 0x0, 0x7]
ddt = generate_ddt(s_box)

print(" --- Difference Distribution Table (DDT) ---")
print("   " + " ".join([f"{i:2}" for i in range(16)]))
for i, row in enumerate(ddt):
    print(f"{i:2}: " + " ".join([f"{val:2}" for val in row]))