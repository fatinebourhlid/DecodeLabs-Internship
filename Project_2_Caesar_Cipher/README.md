# DecodeLabs Cybersecurity Internship - Project 2 🔒

🛡️ **Cryptographic Foundations: Confidentiality & Vulnerability Analysis** **Batch:** 2026 | **Author:** Fatine Bourhlid 

---

## 📋 Overview
This project demonstrates the transition from classical cryptographic algorithms to modern industry-standard protocols. It fulfills the core objectives of Project 2 by implementing robust data obfuscation, demonstrating historical vulnerability analysis (Brute-Force), and deploying enterprise-grade symmetric encryption.

---

## 🛠️ Project Structure

The project has been scaled into three separate functional tools to reflect real-world modular engineering:

1. 🔒 `Caesar_Cipher.py` – Core script handling classical cryptographic encryption and decryption logic using the IPO Model.
2. 🕵️‍♂️ `brute_force.py` – An offensive security tool designed to exploit the mathematical vulnerabilities of historical mono-alphabetic ciphers.
3. 🚀 `AES_encryp.py` – An advanced symmetric encryption pipeline using AES-256 in Galois/Counter Mode (GCM) to ensure both Confidentiality and Authenticated Integrity.

---

## 💻 Implementation Details

### 1. Classical Cryptography: Caesar Cipher
Implements the mathematical substitution cipher using character-to-integer translation (ASCII).

* **Mathematical Formula:** * Encryption: $E_n(x) = (x + n) \pmod{26}$
  * Decryption: $D_n(x) = (x - n) \pmod{26}$

### 2. Offensive Analysis: Brute Force Protocol
Demonstrates the critical vulnerability identified in DecodeLabs materials: **Tiny Key Space**. Because the cipher only has 25 possible keys, an attacker can effortlessly reverse the data in transit by attempting every permutation.

### 3. Modern Protection: Enterprise AES-256 (GCM Mode)
Addresses the "Pattern Preservation" and integrity flaws of historical encryption by implementing:
* **256-bit Key:** Generates a secure 32-byte key using `get_random_bytes(32)`, making brute-force attacks mathematically impossible.
* **Nonce (Number Used Once):** Prevents pattern preservation. Even if the same plaintext is encrypted multiple times, the output remains uniquely random.
* **Authenticated Encryption (GCM):** Generates an **Auth Tag** to verify data integrity, ensuring any unauthorized modifications f transit are immediately detected.

---

## 🚀 How to Run the Lab

### Prerequisites
Install the required production-grade library:

pip install pycryptodome
---

### Author
Fatine Bourhlid Cybersecurity Engineering Student Intern at DecodeLabs

🔗 GitHub: https://github.com/fatinebourhlid

🔗 LinkedIn: https://www.linkedin.com/in/fatine-bourhlid-8a157b291/
