#!/usr/bin/env python
# coding=utf-8


class Solution:
    def reverseBit(self, n):
        dec2bin = bin(n)
        newBin = dec2bin[::-1][:-2]
        if len(newBin) < 32:
            newBin += '0' * (32 - len(newBin))
        newDec = int(newBin, 2)
        return newDec
