# Cryptographic Phase: Basic Encryption & Decryption 🔒

Welcome to my submission for **Project 2** of the Cybersecurity Industrial Training Program at **DecodeLabs** (Batch 2026). This project implements the fundamental mechanics of data confidentiality using symmetric key encryption through a Python-based **Caesar Cipher** engine.

---

## 🛠️ System Architecture (IPO Model)

The application adheres strictly to the universal **Input-Process-Output (IPO)** architecture of cryptographic systems:

1. **INPUT:** Accepts raw user text (Plaintext) and a customizable mathematical shift integer (Key).
2. **PROCESS:** Performs mono-alphabetic substitution logic based on ASCII transformations and modular arithmetic.
3. **OUTPUT:** Generates and displays both the obfuscated ciphertext and the reverse-engineered plaintext for verification.

---

## 🔬 Mathematical Logic

The cryptographic engine maps characters to integers using their ASCII values and processes them with finite alphabet wrapping:

* **Encryption Formula:** 
  $$E_n(x) = (x + n) \pmod{26}$$

* **Decryption Formula:** 
  $$D_n(x) = (x - n) \pmod{26}$$

### Implementation Details:
* **Base Offsets:** Standardized to ASCII base `65` for Uppercase (`A-Z`) and `97` for Lowercase (`a-z`).
* **Edge Case Handling:** All non-alphabetic characters (spaces, numbers, and punctuation) are preserved and bypass the shift logic dynamically.

---

## 🚀 How To Run

### Prerequisites
* Python 3.x installed on your environment.

### Author
Fatine Bourhlid Cybersecurity Engineering Student Intern at DecodeLabs

🔗 GitHub: https://github.com/fatinebourhlid
🔗 LinkedIn: https://www.linkedin.com/in/fatine-bourhlid-8a157b291/