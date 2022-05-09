#!/usr/bin/env python
# coding=utf-8
import time
import os
import sys
import transpositionEncrypt
import transpositionDecrypt


def main():
#    inputFilename = 'frankenstein.txt'
    inputFilename = 'frankenstein.encrypted.txt'
    # be careful! if a file with the outputFilename name already exityts
    # this program will overtime that file
#    outputFilename = 'frankenstein.encrypted.txt'
    outputFilename = 'frankenstein.decrypted.txt'
    myKey = 10
#    myMode = 'encrypt'
    myMode = 'decrypt'

    # if the input file does not exist, the program terminates early
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quiting...' % (inputFilename))
        sys.exit()

    # if the output file already exists, give the user a chance to quit
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
        reponse = input('> ')
        if not reponse.lower().startswith('c'):
            sys.exit()

    # read in the message from the input file
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (myMode.title()))

    # measure how long the encrytion/decrytion takes
    startTime = time.time()
    if myMode == 'encrypt':
        translated = transpositionEncrypt.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpositionDecrypt.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (myMode.title(), totalTime))

    # write out the translated message to the output file
    outputFilenObj = open(outputFilename, 'w')
    outputFilenObj.write(translated)
    outputFilenObj.close()

    print('Done %sing %s (%s characters).' % (myMode, inputFilename,
                                             len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))


if __name__ == '__main__':
    main()
