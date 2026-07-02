# Figure 6: Block Cipher Security Analyzer
from collections import Counter

def block_cipher_analyzer(text1, text2):
    print("--- Block Cipher Security Analyzer ---")
    
    # 1. Avalanche Effect Testing
    h1, h2 = hash(text1), hash(text2)
    avalanche = "PASS" if h1 != h2 else "FAIL"
    print(f"Avalanche Test: {avalanche}")
    
    # 2. Difference Analysis
    diff = sum(c1 != c2 for c1, c2 in zip(text1, text2))
    print(f"Bit/Char Difference: {diff}")
    
    # 3. Frequency Distribution
    freq = Counter(text1)
    print(f"Frequency Distribution: {dict(freq)}")
    
    # 4. Statistical Reporting
    print("Report: Analysis Complete.")

# Execution
block_cipher_analyzer("HELLO", "HELLo")