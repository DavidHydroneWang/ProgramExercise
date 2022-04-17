#!/usr/bin/env python
# coding=utf-8
"""
Pig Latin, by Al Sweigart al@inventwithpython.com
Translates English messages into Igpay Atinlay.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, word
"""

try:
    import pyperclip
except ImportError:
    pass

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')


def main():
    print('''
          Igpay Atinlay (Pig Latin)
          By Al Sweigart al@inventwithpython.com

          Enter your message:
          ''')
    pigLatin = englishToPigLation(input('> '))

    # join all the words back together into a single string.
    print(pigLatin)

    try:
        pyperclip.copy(pigLatin)
        print('(Copied pig latin to clipboard.)')
    except NameError:
        pass


def englishToPigLation(message):
    pigLatin = ''
    for word in message.split():
        # separate the non-letters at the start of this word
        prefixNonLetters = ''
        while len(word) > 0 and not word[0].isalpha():
            prefixNonLetters += word[0]
            word = word[1:]
        if len(word) == 0:
            pigLatin = pigLatin + prefixNonLetters + ' '
            continue

        # separate the non-letters at the end of this word.
        suffixNonLetters = ''
        while not word[-1].isalpha():
            suffixNonLetters = word[-1] + suffixNonLetters
            word = word[:-1]

        # remember if the word was in uppercase or titlecase.
        wasUpper = word.isupper()
        wasTitle = word.istitle()

        word = word.lower()

        # sepatate the constants at the start of this word.
        prefixConstants = ''
        while len(word) > 0 and not word[0] in VOWELS:
            prefixConstants += word[0]
            word = word[1:]

        # add the pig latin ending to the word.
        if prefixConstants != '':
            word += prefixConstants + 'ay'
        else:
            word += 'yay'

        # set the word back to uppercase or titlecase.
        if wasUpper:
            word = word.upper()
        if wasTitle:
            word = word.title()

        # add the non-letters back to the start or end of the word.
        pigLatin += prefixNonLetters + word + suffixNonLetters + ' '
    return pigLatin


if __name__ == '__main__':
    main()
