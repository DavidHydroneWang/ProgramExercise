#!/usr/bin/env python
# coding=utf-8


class Solution:
    def hammingWeight(self, n):
        bList = list(bin(n))
        sumall = 0
        while bList:
            c = bList.pop()
            if c == '1':
                sumall += c
        return sumall
