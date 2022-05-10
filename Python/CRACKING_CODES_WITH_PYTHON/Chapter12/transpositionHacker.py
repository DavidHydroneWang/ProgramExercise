#!/usr/bin/env python
# coding=utf-8
import pyperclip
import sys
import detectEnglish
import transpositionDecrypt


def main():
    # you might want to copy & paste this text from the source code ar
    # https://www.notarch.com/crackingcodes/
    myMessage = """
    AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh
    na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no
    euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain
    one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp
    ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh
    gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr
    aBercaeu thllnrshicwsg etriebruaisss  d iorr.
    """

    hackMessage = hacktransposition(myMessage)

    if hackMessage is None:
        print('Failed to hack encryption.')
    else:
        print('Coping hacked message to clipboard:')
        print(hackMessage)
        pyperclip.copy(hackMessage)


def hacktransposition(message):
    print('Hacking...')

    # python programs can be stopped at any time by pressing
    # Ctrl-C (on Windows) or Ctrl-D (on Macos and Linux)
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')
    # brute-force by looping through every possible key
    for key in range(1, len(message)):
        print('Trying key #%s...' % (key))
        sys.stdout.flush()

        decryptedText = transpositionDecrypt.decryptMessage(key, message)
        englishPercentage = round(detectEnglish.getEnglishCount(decryptedText) * 100, 2)
        sys.stdout.flush()

        if englishPercentage > 20:
            # ask user if this is the correct decryption
            print()
            print('Possible encrption hack:')
            print('Key %s: %s' % (key, decryptedText[:100]))
            print()
            print('Enter D if done, anything else to continue hacking:')
            response = input('> ')
            if response.strip().upper().startswith('D'):
                return decryptedText

    return None


if __name__ == '__main__':
    main()
