#!/usr/bin/env python
# coding=utf-8
import math
import pyperclip


def main():
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8

    plaintext = decryptMessage(myKey, myMessage)

    # print with a | (called "pipe" character) after it in case
    # there are spaces at the end of the decrypted message
    print(plaintext + '|')

    pyperclip.copy(plaintext)


def decryptMessage(key, message):
    # the transposition decrypt function will simulate the "column" and
    # "row" of the grid that the plaintext is written on by using a list
    # of strings. First, we need to calculate a few values

    # the number of "column" in our transposition grid
    numOfColumns = int(math.ceil(len(message) / float(key)))
    # the number of "rows" in our grid
    numOfRows = key
    # the number of "shaded boxes" in the last "column" of the grid
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # each string in plaintext represents a column in the grid
    plaintext = [''] * numOfColumns

    # the column and row variables point to where in the grid the next
    # character in the encrypted message will go
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1

        # if there are no more columns OR we're at a shaded box, go back
        # to the first column and the next row
        if (column == numOfColumns) or \
           (column == numOfColumns - 1 and
            row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    return ''.join(plaintext)


if __name__ == '__main__':
    main()
