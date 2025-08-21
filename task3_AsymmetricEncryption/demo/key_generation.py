from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
import os

def generate_rsa_keys(key_size=2048):
    """
    Generate RSA public and private keys
    """
    # Generate private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
        backend=default_backend()
    )
    
    # Derive public key
    public_key = private_key.public_key()
    
    return private_key, public_key

def save_keys(private_key, public_key, private_key_file="private_key.pem", public_key_file="public_key.pem"):
    """
    Save keys to PEM files
    """
    # Save private key
    with open(private_key_file, "wb") as f:
        f.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
        )
    
    # Save public key
    with open(public_key_file, "wb") as f:
        f.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )
    
    print(f"Keys saved to {private_key_file} and {public_key_file}")

def load_private_key(key_file="private_key.pem"):
    """
    Load private key from file
    """
    with open(key_file, "rb") as f:
        private_key = serialization.load_pem_private_key(
            f.read(),
            password=None,
            backend=default_backend()
        )
    return private_key

def load_public_key(key_file="public_key.pem"):
    """
    Load public key from file
    """
    with open(key_file, "rb") as f:
        public_key = serialization.load_pem_public_key(
            f.read(),
            backend=default_backend()
        )
    return public_key

if __name__ == "__main__":
    # Generate and save demo keys
    private_key, public_key = generate_rsa_keys()
    save_keys(private_key, public_key)
    print("RSA key pair generated successfully!")