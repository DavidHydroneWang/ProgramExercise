#!/usr/bin/env python
# coding=utf-8
"""
"Water Bucket Puzzle, by Al Sweigart al@inventwithpython.com
A water pouring puzzle.
More info: https://en.wikipedia.org/wiki/Water_pouring_puzzle
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, game, math, puzzle
"""

import sys

print('Water Bucket Puzzle,  by Al Sweigart al@inventwithpython.com')

GOAL = 4
steps = 0

# the amount of water in each bucket.
waterBucket = {'8': 0, '5': 0, '3': 0}

while True:
    # display the current state of the bucket.
    print()
    print('Try to get ' + str(GOAL) + 'L of water into one of these')
    print('buckets.')

    waterDisplay = []

    # get the strings for the 8L bucket.
    for i in range(1, 9):
        if waterBucket['8'] < i:
            waterDisplay.append('      ')
        else:
            waterDisplay.append('WWWWWW')

    # get the strings for the 5L bucket.
    for i in range(1, 6):
        if waterBucket['5'] < i:
            waterDisplay.append('      ')
        else:
            waterDisplay.append('WWWWWW')

    # get the strings for the 3L bucket.
    for i in range(1, 4):
        if waterBucket['3'] < i:
            waterDisplay.append('      ')
        else:
            waterDisplay.append('WWWWWW')

    # display the buckets with the amount of water in each one.
    print('''
8|{7}|
7|{6}|
6|{5}|
5|{4}|  5|{12}|
4|{3}|  4|{11}|
3|{2}|  3|{10}|  3|{15}|
2|{1}|  2|{9}|  2|{14}|
1|{0}|  1|{8}|  1|{13}|
 +------+   +------+   +------+
    8L         5L         3L
          '''.format(*waterDisplay))

    # check if any of the buckets has the goal amount of water.
    for waterAmount in waterBucket.values():
        if waterAmount == GOAL:
            print('Good job! You solved it in', steps, 'steps!')
            sys.exit()

    # let the player select an action to do with a bucket.
    print('You can:')
    print('  (F)ill the bucket')
    print('  (E)mpty the bucket')
    print('  (P)our one bucket into another')
    print('  (Q)uit')

    while True:
        move = input('> ').upper()
        if move == 'QUIT' or move == 'Q':
            print('Thanks for playing!')
            sys.exit()

        if move in ('F', 'E', 'P'):
            break
        print('Enter F, E, P, or Q.')

    # let the player select a bucket.
    while True:
        print('select a bucket 8, 5, 3, or QUIT:')
        srcBucket = input('> ').upper()

        if srcBucket == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if srcBucket in ('8', '5', '3'):
            break

    # carry out the selected action
    if move == 'F':
        srcBucketSize = int(srcBucket)
        waterBucket[srcBucket] = srcBucketSize
        steps += 1

    elif move == 'E':
        waterBucket[srcBucket] = 0
        steps += 1

    elif move == 'P':
        while True:
            print('select a bucket to pour into 8, 5, 3')
            dstBucket = input('> ').upper()
#            print(dstBucket)
            if dstBucket in ('8', '5', '3'):
                break

        # figure out the amount to pour.
        dstBucketSize = int(dstBucket)
        emptySpaceInDstBucket = dstBucketSize - waterBucket[dstBucket]
#        print(emptySpaceInDstBucket)
        waterInSrcBucket = waterBucket[srcBucket]
#        print(waterInSrcBucket)
        amountToPour = min(emptySpaceInDstBucket, waterInSrcBucket)
#        print(amountToPour)

        # pour out water from this bucket.
        waterBucket[srcBucket] -= amountToPour
#        print(waterBucket[srcBucket])

        # put the poured out water into the other bucket.
        waterBucket[dstBucket] += amountToPour
#        print(waterBucket[dstBucket])

        steps += 1

    elif move == 'C':
        pass
