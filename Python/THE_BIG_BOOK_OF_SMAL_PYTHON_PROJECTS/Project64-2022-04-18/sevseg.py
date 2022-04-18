#!/usr/bin/env python
# coding=utf-8
"""
Sevseg, by Al Sweigart al@inventwithpython.com
A seven-segment number display module, used by the Countdown and Digital
Clock programs.
More info at https://en.wikipedia.org/wiki/Seven-segment_display
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, module
"""

"""A labeled seven-segment display, with each segment labeled A to G:
 __A__
|     |    Each digit in a seven-segment display:
F     B     __       __   __        __   __  __   __   __
|__G__|    |  |   |  __|  __| |__| |__  |__    | |__| |__|
|     |    |__|   | |__   __|    |  __| |__|   | |__|  __|
E     C
|__D__|"""


def getSevSegStr(number, minWidth=0):
    """
    Return a seven-segment display string of number. The returned
    string will be padded with zeros if it is smaller than minWidth.
    """

    # convert number to string in case it's an int or float.
    number = str(number).zfill(minWidth)

    rows = ['', '', '']
    for i, numeral in enumerate(number):
        if numeral == '.':
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
            continue
        elif numeral == '-':
            rows[0] += '    '
            rows[1] += ' __ '
            rows[2] += '    '
        elif numeral == '0':
            rows[0] += ' __ '
            rows[1] += '|  |'
            rows[2] += '|__|'
        elif numeral == '1':
            rows[0] += '    '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '2':
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += '|__ '
        elif numeral == '3':
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += ' __|'
        elif numeral == '4':
            rows[0] += '   '
            rows[1] += '|__|'
            rows[2] += '   |'
        elif numeral == '5':
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += ' __|'
        elif numeral == '6':
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += '|__|'
        elif numeral == '7':
            rows[0] += ' __ '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '8':
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += '|__|'
        elif numeral == '9':
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += ' __|'

        # add a space (for the space in between numerals) if this
        # isn't the last numeral.
        if i != len(number) - 1:
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '
        return '\n'.join(rows)


# if this program isn't being imported, display the numbers 00 to 99.
if __name__ == '__main__':
    print('This module is meant to be imported rather than run.')
    print('For example, this code:')
    print('    import sevseg')
    print('    myNumber = sevseg.getSevSegStr(42, 3)')
    print('    print(myNumber)')
    print()
    print('will print 42, zero-padded to three digits:')
    print(' __        __ ')
    print('|  | |__|  __|')
    print('|__|    | |__ ')
