#!/usr/bin/env python
# coding=utf-8


import timeit


def countPrime(n):
    primesList = []
    for i in range(2, n + 1):
        flag = True
        for divNum in range(2, i):
            if i % divNum:
                flag = False
                break
        if flag:
            primesList.append(i)
    return len(primesList)


def countPrime(n):
    if n < 2:
        return 0
    elif n == 3:
        return 1
    elif n == 4:
        return 2
    primesList = list(range(2, n))
    multList = []
    for i in range(0, n // 2 + 1):
        multList += list(range(primesList[i], n + 1))[::primesList[i]][1::]
    primesList = list(set(primesList) - set(multList))
    primesList.sort()
    return len(primesList)


def countPrime(n):
    if n < 3:
        return 0
    boolList = [True] * n
    boolList[0] = False
    boolList[1] = False
    for i in range(2, int(pow(n, 0.5) + 1)):
        if boolList[i]:
            boolList[i::i] = [False] * len(boolList[i::i])
            boolList[i] = True
    return sum(boolList)
