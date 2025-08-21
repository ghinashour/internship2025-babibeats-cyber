# Task 2 – Symmetric Encryption (Theory + Demo)

## 1. What is Symmetric Encryption?

Symmetric encryption is a cryptographic technique where the **same key** is used for both **encryption** (locking the data) and **decryption** (unlocking it).  
It is fast, efficient, and suitable for encrypting large amounts of data.

The main challenge is **key distribution**, since both sender and receiver must securely share the secret key.

---

## 2. Common Symmetric Algorithms

- **AES (Advanced Encryption Standard)** → Modern standard, very secure, supports 128, 192, and 256-bit keys.
- **DES (Data Encryption Standard)** → Outdated and insecure due to short 56-bit key size.
- **3DES (Triple DES)** → More secure than DES but slower, being phased out.
- **Blowfish / Twofish** → Flexible key sizes, alternatives to AES.

---

## 3. Recommended for BabiBeats

As a **music streaming platform**, BabiBeats needs to secure both **user data** and **artist content**.  
The recommended encryption is **AES-256 (Advanced Encryption Standard with a 256-bit key)** because:

✅ Industry standard (used in banking, cloud, VPNs)  
✅ Fast enough for large music files  
✅ Strong resistance against brute-force attacks

**Use cases for BabiBeats:**

1. **User Data Protection** → Encrypt sensitive information like payment details.
2. **Music File Security** → Encrypt uploaded tracks to protect against piracy.
3. **API Communication** → Use AES along with TLS for secure data transfer.
