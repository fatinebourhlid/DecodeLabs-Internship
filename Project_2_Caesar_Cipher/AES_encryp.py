import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

print("=========================================")
print("     DECODELABS AES-256 ENGINE V1.0      ")
print("=========================================")

secret_key = get_random_bytes(32) 
print(f"[✓] Generated 256-bit Key (Hex): {secret_key.hex()}")


plaintext = input("\n[>] Enter plaintext to encrypt: ").encode('utf-8')
print("\n--- INITIATING AES ENCRYPTION PROTOCOL ---")

cipher_encrypt = AES.new(secret_key, AES.MODE_GCM)

# Nonce (Number used once) is mandatory in AES to prevent pattern preservation!
nonce = cipher_encrypt.nonce
ciphertext, auth_tag = cipher_encrypt.encrypt_and_digest(plaintext)

print(f"[+] Nonce (Hex):       {nonce.hex()}")
print(f"🔒 Ciphertext (Hex):  {ciphertext.hex()}")
print(f"[+] Auth Tag (Hex):    {auth_tag.hex()}")
print("------------------------------------------")

print("\n--- INITIATING AES DECRYPTION PROTOCOL ---")

try:
    # To decrypt, we MUST provide the exact same Key, Mode, and Nonce
    cipher_decrypt = AES.new(secret_key, AES.MODE_GCM, nonce=nonce)
    
    # Decrypt and verify integrity using the Auth Tag
    decrypted_bytes = cipher_decrypt.decrypt_and_verify(ciphertext, auth_tag)
    decrypted_text = decrypted_bytes.decode('utf-8')
    
    print(f"🔓 Decrypted Plaintext: {decrypted_text}")
    print("[✓] Integrity Verified: Data has not been modified.")

except ValueError:
    print("[X] CRITICAL ERROR: Decryption failed or Ciphertext was tampered with!")

print("=========================================")