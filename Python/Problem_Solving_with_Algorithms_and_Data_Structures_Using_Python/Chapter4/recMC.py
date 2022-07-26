#!/usr/bin/env python
# coding=utf-8


def recMc(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMc(coinValueList, change - i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins


result = recMc([1, 5, 10, 25], 63)
print(result)
