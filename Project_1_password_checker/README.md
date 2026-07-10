# Project 1: DecodeLabs Gatekeeper (Defensive Password Analyzer)

An enterprise-grade, highly efficient **Password Strength Checker** developed following defensive coding practices and structural security architecture guidelines. This component acts as a rigorous **Gatekeeper** to enforce security policies prior to structural data processing or cryptographic hashing pipelines (e.g., Argon2id).

---

## 🏗️ Structural Architecture (IPO Model)

The script processes data linearly ensuring validation time grows linearly ($O(n)$ Scan time complexity) and never exponentially, completely mitigating potential resource exhaustion vectors (DoS).


    [INPUT]  --------->      [PROCESS]       --------->   [OUTPUT]
 Raw Byte Stream       C-Optimized Short-Circuit      Risk Classification
   (Password)              Linear O(n) Scan               (Pass/Fail)
   
## 🔓 Security Policy Requirements
Length Verification: Passwords < 8 characters trigger an Immediate Fail to completely eliminate exponential brute-force risk profiles.

Pattern Recognition: Mandatory enforcement of Uppercase [A-Z], Lowercase [a-z], Digits [0-9], and Special Symbols.

The Unicode Curveball: Expanded search space scanning from 95 characters (ASCII) to 143,000+ characters (Unicode) to handle modern inputs (e.g., Emojis 🕶️) seamlessly.

## 🛠️ Core Security Engineering Principles
This implementation directly maps defensive design choices against real-world vulnerability patterns:

Computational Efficiency (Pythonic Elegance): Built using highly optimized, short-circuiting Python built-ins (any()). The validation logic halts processing the microsecond a rule criterion is fulfilled, ensuring execution speed is scale-linear and robust against execution-denial vectors.

The Volatile Security Trap (Data in RAM): Standard string handling leaves lingering data in heap memory until arbitrary Garbage Collection occurs. This architecture isolates input streams to minimize the footprint exposed to RAM Scraping malware (e.g., BlackPOS).

Advanced Vulnerability Mitigation (Timing Attacks): Early rejections on empty/short strings prevent information leaks regarding secret lengths, ensuring standard processing windows remain stable.

## 🚀 Installation & Local Execution
Ensure you have a modern Python environment active, then run the structural defensive analyzer locally:

Bash
# Navigate to the project directory
cd Project_1_Gatekeeper

# Run the analyzer script
python password_checker.py
Developed under DecodeLabs Track Regulations for Applied Security Engineering.
