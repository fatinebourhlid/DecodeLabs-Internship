def encrypt_caesar(text, shift):
    cipher_text = ""
    for char in text:
        if char.isupper():
            cipher_char = chr((ord(char) - 65 + shift) % 26 + 65)
            cipher_text += cipher_char
        elif char.islower():
            cipher_char = chr((ord(char) - 97 + shift) % 26 + 97)
            cipher_text += cipher_char
        else:
            cipher_text += char
    return cipher_text

def decrypt_caesar(cipher_text, shift):
    return encrypt_caesar(cipher_text, -shift)

user_text = input("Entrez votre text: ")
shift_key = int(input("Entrez Shift Key: "))
encrypted_msg = encrypt_caesar(user_text, shift_key)
decrypted_msg = decrypt_caesar(encrypted_msg, shift_key)

print("\n--- RESULTS ---")
print(f"📄 Original Text:  {user_text}")
print(f"🔒 Encrypted Text: {encrypted_msg}")
print(f"🔓 Decrypted Text: {decrypted_msg}")