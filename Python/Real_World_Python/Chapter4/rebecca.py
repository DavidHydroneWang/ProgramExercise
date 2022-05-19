#!/usr/bin/env python
# coding=utf-8
import sys
import os
import random
from collections import defaultdict, Counter


def main():
    message = input('Enter plaintext or ciphertext: ')
    process = input("Enter 'encrypt' or 'decrypt': ")
    while process not in ('encrypt', 'decrypt'):
        process = input("invalid process: Enter 'encrypt' or 'dectrypt': ")
    shift = int(input("Shift value (1-366) = "))
    while not 1 <= shift <= 366:
        shift = int(input("Invalid value: Enter digit from 1 to 366: "))
    infile = input("Enter filename with extension: ")
    if not os.path.exists(infile):
        print("File {} not Found. Terminating.".format(infile),
              file=sys.stderr)
        sys.exit(1)
    text = load_file(infile)
    char_dict = make_dict(text, shift)

    if process == 'encrypt':
        ciphertext = encrypt(message, char_dict)

        # run QC protocols and print results
        if check_for_fail(ciphertext):
            print("\nProblem finding unique keys.", file=sys.stderr)
            print("Try again, change message, or change code book.\n",
                  file=sys.stderr)
            sys.exit()

        print("\nCharacter and number of occurrence in char_dict: \n")
        print("{: >10}{: >10}".format('Character', 'Unicode', 'Count'))
        for key in sorted(char_dict.keys()):
            print('{:>10}{:>10}{:>10}'.format(repr(key)[1:-1],
                                              str(ord(key)),
                                              len(char_dict[key])))
        print('\nNumber of distinct characters: {}'.format(len(char_dict)))
        print("Total number of characters: {:,}\n".format(len(text)))

        print("encrypted ciphertext = \n {} \n".format(ciphertext))

        # check the encryption by decrypting the ciphertext
        print("decrypted plaintext =")
        for i in ciphertext:
            print(text[i - shift], end='', flush=True)

    elif process == 'decrypt':
        plaintext = decrypt(message, text, shift)
        print("\ndecrypted plaintext = \n {}".format(plaintext))


def load_file(infile):
    """read and return text file as a string of lowercase characters."""
    with open(infile, encoding='utf-8', errors='ignore') as f:
        load_string = f.read().lower()
    return load_string


def make_dict(text, shift):
    """return dictionary of characters as keys and shifted indexes as values"""
    char_dict = defaultdict(list)
    for index, char in enumerate(text):
        char_dict[char].append(index + shift)
    return char_dict


def encrypt(message, char_dict):
    """return list of indexes representing characters in a message."""
    encrypted = []
    for char in message.lower():
        if len(char_dict[char]) > 1:
            index = random.choice(char_dict[char])
        elif len(char_dict[char]) == 1:
            index = char_dict[char][0]
        elif len(char_dict[char]) == 0:
            print("\nCharacter {} not in dictionary.".format(char),
                  file=sys.stderr)
            continue
        encrypted.append(index)
    return encrypted


def decrypt(message, text, shift):
    """decrypt ciphertext list and return plaintext string"""
    plaintext = ''
    indexes = [s.replace(',', '').replace('[', '').replace(']', '')
               for s in message.split()]
    for i in indexes:
        plaintext += text[int(i) - shift]
    return plaintext


def check_for_fail(ciphertext):
    """return True if ciphertext contains any duplicate keys"""
    check = [k for k, v in Counter(ciphertext).items() if v > 1]
    if len(check) > 0:
        return True


if __name__ == '__main__':
    main()
