#!/usr/bin/env python
# coding=utf-8
import math
from string import punctuation
import nltk
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


PUNCT_SET = set(punctuation)


def main():
    strings_by_author = dict()
    strings_by_author['doyle'] = text_to_string('hound.txt')
    strings_by_author['wells'] = text_to_string('war.txt')
    strings_by_author['unknown'] = text_to_string('lost.txt')

    # tokenize text strings preserving only punctuation marks
    punct_by_author = make_punct_dict(strings_by_author)

    # convert punctuation marks to numerical values and plot heatmaps
    plt.ion()
    for author in punct_by_author:
        heat = convert_punct_to_number(punct_by_author, author)
        arr = np.array((heat[:6561]))
        arr_reshaped = arr.reshape(int(math.sqrt(len(arr))),
                                   int(math.sqrt(len(arr))))
        fig, ax = plt.subplots(figsize=(7, 7))
        sns.heatmap(arr_reshaped,
#                    cmap=ListedColormap(['blue', 'yellow']),
                    square=True,
                    ax=ax)
        ax.set_title('Heatmap Semicolons {}'.format(author))
    plt.show()


def text_to_string(filename):
    """Read a text file and return a string."""
    with open(filename, encoding='utf-8', errors='ignore') as infile:
        return infile.read()


def make_punct_dict(strings_by_author):
    """return dictionary of tokenize punctuation by copus by author"""
    punct_by_author = dict()
    for author in strings_by_author:
        tokens = nltk.word_tokenize(strings_by_author[author])
        punct_by_author[author] = ([token for token in tokens
                                    if token in PUNCT_SET])
        print('Number punctuation marks in {} = {}'.format(author,
                                                           len(punct_by_author[author])))
    return punct_by_author


def convert_punct_to_number(punct_by_author, author):
    """return list of punctuation marks converted to numerical values"""
    heat_vals = []
    for char in punct_by_author[author]:
        if char == ';':
            value = 1
        else:
            value = 2
        heat_vals.append(value)
    return heat_vals


if __name__ == '__main__':
    main()
