flowchart TD
A["Original Song File / User Data"] --> B["AES Encryption<br/>(Key + Initialization Vector)"]
B --> C["Encrypted Secure Data"]
C --> D["AES Decryption<br/>(Same Key + IV required)"]
D --> E["Original Content Restored"]
