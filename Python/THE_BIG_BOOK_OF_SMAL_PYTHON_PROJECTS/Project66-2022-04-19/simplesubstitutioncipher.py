#!/usr/bin/env python
# coding=utf-8
"""
Simple Substitution Cipher, by Al Sweigart al@inventwithpython.com
A simple substitution cipher has a one-to-one translation for each
symbol in the plaintext and each symbol in the ciphertext.
More info at: https://en.wikipedia.org/wiki/Substitution_cipher
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, cryptography, math
"""

import random

try:
    import pyperclip
except ImportError:
    pass

# every possible symbol that can be encrpted/decrypted.
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    print('''
          Simple Substitution Cipher, by Al Sweigart
          A simple substitution cipher has a one-to-one translation for each
          symbol in the plaintext and each symbol in the ciphertext.
          ''')
    # let the user specify if they are encrypting or decrypting.
    while True:
        print('Do you want to (e)ncrypt or (d)ecrypt?')
        response = input('> ').lower()
        if response.startswith('e'):
            myMode = 'encrypt'
            break
        elif response.startswith('d'):
            myMode = 'decrypt'
            break
        print('Please enter the letter e or d.')

    # let the user specify the key to use.
    while True:
        print('Please specify the key to use.')
        if myMode == 'encrypt':
            print('Or enter RANDOM to have one generate for you.')
        response = input('> ').upper()
        if response == 'RANDOM':
            myKey = generateRandomKey()
            print('The key is {}. KEEP THIS SECRET!'.format(myKey))
            break
        else:
            if checkKey(response):
                myKey = response
                break

    # let the user specify the message to encrypt/decrypt.
    print('Enter the message to {}.'.format(myMode))
    myMessage = input('> ')

    # perform the encryption/decryption.
    if myMode == 'encrypt':
        translated = encryptMessage(myMessage, myKey)
    elif myMode == 'decrypt':
        translated = decryptMessage(myMessage, myKey)
    # display the results.
    print('The %sed message is: ' % (myMode))
    print(translated)

    try:
        pyperclip.copy(translated)
        print('Full %sed text copied to clipboard.' % (myMode))
    except:
        pass


def checkKey(key):
    """returns True if key is valid. otherwise return False."""
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        print('There is an error in the key or symbol set.')
        return False
    return True


def encryptMessage(message, key):
    """encrypt the message using the key."""
    return translateMessage(message, key, 'encrypt')


def decryptMessage(message, key):
    """decrypt the message using the key."""
    return translateMessage(message, key, 'decrypt')


def translateMessage(message, key, mode):
    """encrypt or decrypt the message using the key."""
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA

    # loop through each symbol in the message.
    for symbol in message:
        if symbol.upper() in charsA:
            # encrypt/decrypt the symbol
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # the symbol is not in LETTERS, just add it unchanged.
            translated += symbol
    return translated


def generateRandomKey():
    """generate and return a random encryption key."""
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


# if this program was run (instead of imported), run the program
if __name__ == '__main__':
    main()
