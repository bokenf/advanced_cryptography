# Figure 4: Frequency Analysis
from collections import Counter

data = "ABABABABCCCCDDD"

# Perform frequency analysis
count = Counter(data)

print("--- Frequency Analysis ---")
print(f"Data: {data}")
print(f"Distribution: {dict(count)}")