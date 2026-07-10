import string

class PasswordStrengthChecker:
    def __init__(self, password: str):
        self.password = password
        self.errors = []

    def is_valid_length(self):
        return len(self.password) >= 8

    def analyze_strength(self):
        if not self.is_valid_length():
            self.errors.append("CRITICAL: Password is less than 8 characters. Immediate Fail.")
            return "WEAK (Immediate Fail)"

        has_upper   = any(char.isupper() for char in self.password)
        has_lower   = any(char.islower() for char in self.password)
        has_digit   = any(char.isdigit() for char in self.password)
        has_symbol  = any(not char.isalnum() for char in self.password)
        score = sum([has_upper, has_lower, has_digit, has_symbol])

        if score == 4 and len(self.password) >= 12:
            return "STRONG"
        elif score >= 3:
            return "MEDIUM"
        else:
            if not has_upper:  self.errors.append("Missing uppercase letter [A-Z].")
            if not has_lower:  self.errors.append("Missing lowercase letter [a-z].")
            if not has_digit:  self.errors.append("Missing number [0-9].")
            if not has_symbol: self.errors.append("Missing special symbol or Unicode character.")
            return "WEAK"
if __name__ == "__main__":
    print("="*50)
    print("      DECODELABS: PASSWORD STRENGTH CHECKER      ")
    print("="*50)
  
    user_input = input("[+] Enter a password to analyze: ")
    
    analyzer = PasswordStrengthChecker(user_input)
    result = analyzer.analyze_strength()
    
    print(f"\n[*] ANALYSIS RESULT: {result}")
    
    if analyzer.errors:
        print("\n[-] Security Policy Violations Detected:")
        for error in analyzer.errors:
            print(f"    -> {error}")
    else:
        print("\n[+] Gatekeeper Pass: Policy compliance verified.")
    print("="*50)