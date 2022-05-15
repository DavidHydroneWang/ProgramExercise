#!/usr/bin/env python
# coding=utf-8
import pyperclip
import secrets

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    # # This text can be copy/pasted from https://invpy.com/vigenereCipher.py:
    myMessage = """Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist."""
#    myMessage = """Fqgp Ihbrzvlx Fnlxol tum d Vzsvxxz wkczqlmkobxrh, hyxpyhph, oxbabyiudhgp, tib psoxqlhz psrfkggey."""
    myMode = 'encrypt'
#    myMode = 'decrypt'

    if myMode == 'encrypt':
        myKey = ''
        for i in range(len(myMessage)):
            myKey += secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        with open('key.txt', 'w') as file:
            file.write(myKey)
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        with open('key.txt', 'r') as file:
            myKey = file.readline()
            print(myKey)
        translated = decryptMessage(myKey, myMessage)

    print('%sed message:' % (myMode.title()))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('The message has been copied to the clipboard.')


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = []
    keyIndex = 0
    key = key.upper()

    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex])
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex])

            num %= len(LETTERS)

            # add the encrypted/decrypted symbol to the end of translated
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            # append the symbol without encrypting/decrypting.
            translated.append(symbol)

    return ''.join(translated)


if __name__ == '__main__':
    main()