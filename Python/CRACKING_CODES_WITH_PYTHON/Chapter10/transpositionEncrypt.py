#!/usr/bin/env python
# coding=utf-8
import pyperclip


def main():
    myMessage = 'Common sense is not so common.'
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    # print the encrypted string in ciphertext to the screen, with
    # a | ("pipe" character) after it in case there are spaces at
    # the end of the encrypted message:
    print(ciphertext + '|')



def encryptMessage(key, message):
    # each string in ciphertext represents a column in the grid
    ciphertext = [''] * key

    # loop through each column in ciphertext
    for column in range(key):
        currentIndex = column

        # keep looping until currentIndex goes past the message length
        while currentIndex < len(message):
            # place the character at currentIndex in message at the
            # end of the current column in the ciphertext list
            ciphertext[column] += message[currentIndex]

            # move currenrtIndex over
            currentIndex += key

    # convert the ciphertext list into a single string value and return it
    return ''.join(ciphertext)


if __name__ == '__main__':
    main()
