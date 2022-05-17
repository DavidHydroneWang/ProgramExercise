#!/usr/bin/env python
# coding=utf-8
import nltk
import file_loader

corpus = file_loader.text_to_string('hound.txt')
tokens = nltk.word_tokenize(corpus)
tokens = nltk.Text(tokens)  # NLTK wrapper for automatic text analysis

dispersion = tokens.dispersion_plot(['Holmes',
                                     'Watson',
                                     'Mortimer',
                                     'Henry',
                                     'Barrymore',
                                     'Stapleton',
                                     'Selden',
                                     'hound'])
