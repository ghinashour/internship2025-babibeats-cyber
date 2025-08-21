# Digital Signatures

## What is a Digital Signature?

A digital signature is a cryptographic technique used to verify the authenticity and integrity of digital data (messages, files, or transactions). It acts like a virtual fingerprint unique to the signer.

## Digital signatures rely on public key cryptography (asymmetric encryption). The signer uses a private key to generate the signature, and anyone with the corresponding public key can verify it.

## Why Use Digital Signatures?

Digital signatures provide three main guarantees:

Authentication – Confirms that the message was created by a known sender (valid identity).

Integrity – Ensures the message has not been altered during transmission.

## Non-repudiation – The signer cannot later deny having signed the message.

## How Digital Signatures Work (Conceptual Flow)

Sender creates a hash of the message.

The hash is encrypted with the sender’s private key, producing the digital signature.

The message and signature are sent together.

The receiver:

Decrypts the signature with the sender’s public key (retrieves the hash).

Independently computes the hash of the received message.

## If both hashes match → the message is authentic and unchanged.
