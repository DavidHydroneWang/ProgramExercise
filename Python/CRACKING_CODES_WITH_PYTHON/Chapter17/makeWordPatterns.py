#!/usr/bin/env python
# coding=utf-8
import pprint


def getWordPattern(word):
    # returns a string of the pattern form of the given word
    # e.g. '0.1.2.3.4.1.2.3.5.6' for 'DUSTBUSTER'
    word = word.upper()
    nextNum = 0
    letterNums = {}
    wordPattern = []

    for letter in word:
        if letter not in letterNums:
            letterNums[letter] = str(nextNum)
            nextNum += 1
        wordPattern.append(letterNums[letter])
    return '.'.join(wordPattern)


def main():
    allPattern = {}

    fo = open('dictionary.txt')
    wordList = fo.read().split('\n')
    fo.close()

    for word in wordList:
        # get the pattern for each string in wordList
        pattern = getWordPattern(word)

        if pattern not in allPattern:
            allPattern[pattern] = [word]
        else:
            allPattern[pattern].append(word)

    # This is code that writes code. The wordPaterns.py file contains
    # one very, very large assignment statement.
    fo = open('wordPattern.py', 'w')
    fo.write('allPattern = ')
    fo.write(pprint.pformat(allPattern))
    fo.close()


if __name__ == '__main__':
    main()
