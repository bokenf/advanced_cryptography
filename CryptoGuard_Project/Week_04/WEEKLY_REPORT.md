# Week 4: Block Ciphers and Modes of Operation

## Title: Analysis and Simulation of Block Cipher Modes

## Required Evidence

**Fig 1: Block Cipher Encryption Logic (ECB vs CBC)**
![CipherLogic](images/fig1.png)

**Fig 2: Initialization Vector (IV) Implementation**
![IV_Logic](images/fig2.png)

**Fig 3: Padding Scheme Demonstration**
![Padding](images/fig3.png)

**Fig 4: Ciphertext Pattern Comparison**
![Pattern](images/fig4.png)

**Fig 5: Decryption Success Results**
![Decryption](images/fig5.png)

## Student Reflection
Block ciphers process data in fixed-size chunks, necessitating padding for non-aligned inputs. Modes like CBC utilize an Initialization Vector (IV) to ensure identical plaintext blocks produce unique ciphertext, preventing the pattern analysis vulnerabilities found in ECB mode. I validated this by comparing ciphertext outputs and verifying integrity.