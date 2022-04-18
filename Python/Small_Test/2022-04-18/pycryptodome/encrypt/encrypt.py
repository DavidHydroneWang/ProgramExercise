#!/usr/bin/env python
# coding=utf-8

from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP


with open('data.bin', 'wb') as output:
    recipient_key = RSA.import_key(
        open('my_rsa_public.pem').read()
    )
    session_key = get_random_bytes(16)

    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    output.write(cipher_rsa.encrypt(session_key))

    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    data = b'wss1996'
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)

    output.write(cipher_aes.nonce)
    output.write(tag)
    output.write(ciphertext)
