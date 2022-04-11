#!/usr/bin/env python
# coding=utf-8
"""
Gullible, by Al Sweigart al@inventwithpython.com
How to keep a gullible person busy for hours. (This is a joke program.)
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, humor
"""

print('Gullible, by Al Sweigart al@inventwithpython.com')

while True:
    print('Do you want to know how to keep a gullible person busy for \
          hours? Y/N')
    reponse = input('> ')
    if reponse.lower() == 'no' or reponse.lower() == 'n':
        break
    if reponse.lower() == 'yes' or reponse.lower() == 'y':
        continue
    print('"{}" is not a valid yes/no response.'.format(reponse))

print('Thank you. Have a nice day!')
