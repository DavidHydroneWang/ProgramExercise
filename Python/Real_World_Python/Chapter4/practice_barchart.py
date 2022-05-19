#!/usr/bin/env python
# coding=utf-8
import sys
import os
import operator
from collections import Counter
import matplotlib.pyplot as plt


def load_file(infile):
    """read and return text file as string of lowercase characters."""
    with open(infile, encoding='utf-8', errors='ignore') as f:
        text = f.read().lower()
    return text


def main():
    infile = 'lost.txt'
    if not os.path.exists(infile):
        print("File {} not found. Terminating.".format(infile),
              file=sys.stderr)
        sys.exit(1)

    text = load_file(infile)

    # make bar chart of characters in text and their frequency
    char_freq = Counter(text)
    char_freq_sorted = sorted(char_freq.items(),
                              key=operator.itemgetter(1), reverse=True)
    x, y = zip(*char_freq_sorted)
    fig, ax = plt.subplots()
    ax.bar(x, y)
    fig.show()


if __name__ == '__main__':
    main()
