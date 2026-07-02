# Week 3: Stream Ciphers and Randomness Testing

## Title: Implementation of Stream Cipher Systems and Random Sequence Analysis

## Required Evidence

**Fig 1: LFSR Generator Implementation**
![LFSR](images/fig1.png)

**Fig 2: Pseudorandom Sequence Output**
![Sequence](images/fig2.png)

**Fig 3: Statistical Randomness Testing**
![Testing](images/fig3.png)

**Fig 4: RC4 Stream Cipher Simulation**
![RC4](images/fig4.png)

**Fig 5: Encryption Performance Results**
![Performance](images/fig5.png)

## Student Reflection
Randomness is the foundation of unpredictability in cryptography. Stream ciphers operate by XORing plaintext with a pseudorandom keystream. I performed frequency testing to verify sequence distribution. Effective pseudorandom generation is critical, as any detectable patterns in the keystream allow for trivial decryption, rendering the encryption scheme entirely insecure.