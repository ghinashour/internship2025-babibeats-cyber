from key_generation import generate_rsa_keys, save_keys, load_private_key, load_public_key
from rsa_encryption import RSAEncryption, encrypt_with_public_key, decrypt_with_private_key

def demo_asymmetric_encryption():
    print("🔐 Asymmetric Encryption Demo")
    print("=" * 50)
    
    # Generate keys
    print("1. Generating RSA key pair (2048-bit)...")
    private_key, public_key = generate_rsa_keys()
    
    # Initialize encryption class
    rsa = RSAEncryption()
    
    # Original message
    original_message = "Hello, this is a secret message for my cybersecurity internship!"
    print(f"2. Original message: {original_message}")
    print()
    
    # Encryption
    print("3. Encrypting with PUBLIC key...")
    encrypted_message = rsa.encrypt_message(public_key, original_message)
    print(f"   Encrypted message (base64): {encrypted_message[:100]}...")
    print()
    
    # Decryption
    print("4. Decrypting with PRIVATE key...")
    decrypted_message = rsa.decrypt_message(private_key, encrypted_message)
    print(f"   Decrypted message: {decrypted_message}")
    print()
    
    # Digital signature demo
    print("5. Digital Signature Demo:")
    document = "Important contract for cybersecurity project"
    print(f"   Document: {document}")
    
    # Create signature
    signature = rsa.create_digital_signature(private_key, document)
    print(f"   Signature: {signature[:80]}...")
    
    # Verify signature
    is_valid = rsa.verify_signature(public_key, document, signature)
    print(f"   Signature valid: {is_valid}")
    
    # Test tampering
    tampered_doc = document + " (tampered)"
    is_valid_tampered = rsa.verify_signature(public_key, tampered_doc, signature)
    print(f"   Tampered signature valid: {is_valid_tampered}")
    print()
    
    print("✅ Demo completed successfully!")

if __name__ == "__main__":
    demo_asymmetric_encryption()