#!/usr/bin/env python
# coding=utf-8
import random


def randomList(n):
    '''a list of length n, n in range(1000)'''
    iList = []
    for i in range(n):
        iList.append(random.randrange(1000))
    return iList


if __name__ == '__main__':
    iList = randomList(20)
    print(iList)
