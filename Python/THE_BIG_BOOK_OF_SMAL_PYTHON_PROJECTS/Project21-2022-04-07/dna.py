#!/usr/bin/env python
# coding=utf-8
"""
DNA, by Al Sweigart al@inventwithpython.com
A simple animation of a DNA double-helix. Press Ctrl-C to stop.
Inspired by matoken https://asciinema.org/a/155441
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, artistic, scrolling, science
"""

import random, sys, time

PAUSE = 0.15  # (!) try changing this to 0.5 or 0.0

# These are the individual rows of the DNA animation.
ROWS = [
    # 123456789<- use this to measure the number of spaces.
    '         ##',  # index 0 has no {}
    '        #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '     #{}------{}#',
    '    #{}------{}#',
    '    #{}-----{}#',
    '     #{}---{}#',
    '     #{}-{}#',
    '      ##',  # index 9 has no {}
    '     #{}-{}#',
    '     #{}---{}#',
    '    #{}-----{}#',
    '    #{}------{}#',
    '     #{}------{}#',
    '      #{}-----{}#',
    '       #{}---{}#',
    '        #{}-{}#'
]   # 123456789<- use this to measure the number of spaces.

try:
    print('DNA Animation, bt Al Sweigart al@inventwithpython.com')
    print('Press Ctrl-C to quit...')
    time.sleep(2)
    rowIndex = 0

    while True:
        # increment rowIndex to draw next row.
        rowIndex = rowIndex + 1
        if rowIndex == len(ROWS):
            rowIndex = 0

        # row indexes 0 and 9 don't have nucleotides.
        if rowIndex == 0 or rowIndex == 9:
            print(ROWS[rowIndex])
            continue

        # select random nucleotide pairs, guanine-cytisine and
        # adenine-thymine.
        randomSelection = random.randint(1, 4)
        if randomSelection == 1:
            leftNucleotide, rightNucleotide = 'A', 'T'
        elif randomSelection == 2:
            leftNucleotide, rightNucleotide = 'T', 'A'
        elif randomSelection == 3:
            leftNucleotide, rightNucleotide = 'C', 'G'
        elif randomSelection == 4:
            leftNucleotide, rightNucleotide = 'G', 'C'

        # print the row.
        print(ROWS[rowIndex].format(leftNucleotide, rightNucleotide))
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()
