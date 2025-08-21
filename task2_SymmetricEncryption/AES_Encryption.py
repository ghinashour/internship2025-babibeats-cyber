from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Generate a random 256-bit (32 bytes) AES key
key = os.urandom(32)

# Generate a random 128-bit (16 bytes) initialization vector (IV)
iv = os.urandom(16)

# Message to encrypt (example: user’s password or a short text)
message = b"Welcome to BabiBeats Secure Streaming!"

# Encrypt
cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(message) + encryptor.finalize()

print("🔐 Encrypted:", ciphertext)

# Decrypt
decryptor = cipher.decryptor()
decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()

print("🔓 Decrypted:", decrypted_message.decode())
