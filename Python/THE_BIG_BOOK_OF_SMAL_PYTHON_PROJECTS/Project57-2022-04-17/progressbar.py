#!/usr/bin/env python
# coding=utf-8
"""
Progress Bar Simulation, by Al Sweigart al@inventwithpython.com
A sample progress bar animation that can be used in other programs.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, module
"""

import random
import time

BAR = chr(9608)


def main():
    # simulate a download
    print('Progress Bar Simulation, by Al Sweigart')
    bytesDownloaded = 0
    downloadSize = 4096
    while bytesDownloaded < downloadSize:
        # ""download"" a random amount of "bytes".
        bytesDownloaded += random.randint(0, 100)
        # get the progress bar string for this amount of progress.
        barStr = getProgressBar(bytesDownloaded, downloadSize)

        # don't print a newline at the end, and immediately flush the
        # printed string, to the screen.
        print(barStr, end='', flush=True)
        time.sleep(0.2)

        # print backspaces to move the text cursor to the line's start.
        print('\b' * len(barStr), end='', flush=True)


def getProgressBar(progress, total, barWidth=40):
    """returns a string that represents a progress bar that has barWidth
    bars and has progressed progress amount out of the progress bar."""
    progressBar = ''
    progressBar += '['

    # make sure that the amount of progress is between 0 and total.
    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    # callculate the number of "bar" to display
    numberOfBars = int((progress / total) * barWidth)

    progressBar += BAR * numberOfBars
    progressBar += ' ' * (barWidth - numberOfBars)
    progressBar += ']'

    # calculate the percentage complete.
    percentComplete = round(progress / total * 100, 1)
    progressBar += ' ' + str(percentComplete) + '%'

    # add the numbers.
    progressBar += ' ' + str(progress) + '/' + str(total)

    return progressBar


# if the program is run (instead of imported), run the game.
if __name__ == '__main__':
    main()
