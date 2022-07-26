#!/usr/bin/env python
# coding=utf-8


def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    for cents in range(change + 1):
        coinCount = cents
        newcoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newcoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newcoin
    return minCoins[change]


def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin -= thisCoin

coinsUsed = [0] * 64
coinCount = [0] * 64
dpMakeChange([1, 5, 10, 21, 25], 63, coinCount, coinsUsed)

printCoins(coinsUsed, 63)
print(coinsUsed)
