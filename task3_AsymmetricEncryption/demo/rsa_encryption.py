from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import base64

class RSAEncryption:
    def __init__(self):
        self.oaep_padding = padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    
    def encrypt_message(self, public_key, message):
        """
        Encrypt message using public key
        """
        if isinstance(message, str):
            message = message.encode('utf-8')
        
        encrypted = public_key.encrypt(
            message,
            self.oaep_padding
        )
        
        return base64.b64encode(encrypted).decode('utf-8')
    
    def decrypt_message(self, private_key, encrypted_message):
        """
        Decrypt message using private key
        """
        if isinstance(encrypted_message, str):
            encrypted_message = base64.b64decode(encrypted_message.encode('utf-8'))
        
        decrypted = private_key.decrypt(
            encrypted_message,
            self.oaep_padding
        )
        
        return decrypted.decode('utf-8')
    
    def create_digital_signature(self, private_key, message):
        """
        Create digital signature using private key
        """
        if isinstance(message, str):
            message = message.encode('utf-8')
        
        signature = private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        
        return base64.b64encode(signature).decode('utf-8')
    
    def verify_signature(self, public_key, message, signature):
        """
        Verify digital signature using public key
        """
        if isinstance(message, str):
            message = message.encode('utf-8')
        
        if isinstance(signature, str):
            signature = base64.b64decode(signature.encode('utf-8'))
        
        try:
            public_key.verify(
                signature,
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False

# Utility function for quick encryption/decryption
def encrypt_with_public_key(public_key, message):
    rsa = RSAEncryption()
    return rsa.encrypt_message(public_key, message)

def decrypt_with_private_key(private_key, encrypted_message):
    rsa = RSAEncryption()
    return rsa.decrypt_message(private_key, encrypted_message)