from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.asymmetric.utils import Prehashed
from cryptography.hazmat.backends import default_backend
import os

def sign_message(private_key, message):
    """Sign a message using PSS padding"""
    try:
        # Create PSS padding instance
        pss_padding = padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        )
        
        # Sign the message
        signature = private_key.sign(
            message,
            pss_padding,
            hashes.SHA256()
        )
        
        return signature
        
    except Exception as e:
        print(f"Signing error: {e}")
        return None

def verify_signature(public_key, message, signature):
    """Verify a signature using PSS padding"""
    try:
        # Create PSS padding instance
        pss_padding = padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        )
        
        # Verify the signature
        public_key.verify(
            signature,
            message,
            pss_padding,
            hashes.SHA256()
        )
        
        return True
        
    except Exception as e:
        print(f"Verification error: {e}")
        return False

# Example usage:
if __name__ == "__main__":
    # Generate keys (in real code, load existing keys)
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    
    # Message to sign
    message = b"Hello, this is a test message"
    
    # Sign the message
    signature = sign_message(private_key, message)
    
    if signature:
        print("Signature created successfully")
        
        # Verify the signature
        is_valid = verify_signature(public_key, message, signature)
        print(f"Signature valid: {is_valid}")