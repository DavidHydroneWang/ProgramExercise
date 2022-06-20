#!/usr/bin/env python
# coding=utf-8
from randomList import randomList
import timeit


iList = randomList(20)


def selectionSort(iList):
    if len(iList) <= 1:
        return iList
    for i in range(len(iList) - 1):
        if iList != min(iList[:]):
            minIndex = iList.index(min(iList[:]))
            iList[i], iList[minIndex] = iList[minIndex], iList[i]
    return iList


if __name__ == '__main__':
    print(iList)
    print(selectionSort(iList))
    print(timeit.timeit('selectionSort(iList)', 'from __main__\
                        import selectionSort, iList', number=100))
