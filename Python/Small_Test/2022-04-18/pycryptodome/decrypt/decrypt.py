#!/usr/bin/env python
# coding=utf-8
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

code = 'weffhyyhjj'

with open('data.bin', 'rb') as data:
    private_key = RSA.import_key(
        open('my_private_rsa_key.bin').read(),
        passphrase=code
    )
    enc_session_key, nonce, tag, ciphertext = [
        data.read(x)
        for x in (private_key.size_in_bytes(), 16, 16, -1)
    ]
    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    result = cipher_aes.decrypt_and_verify(ciphertext, tag)

print(result)
