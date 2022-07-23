#!/usr/bin/env python
# coding=utf-8


class Solution:
    def generate(self, numRows):
        rList = []
        for i in range(1, numRows + 1):
            tempList = i * [None]
            tempList[0] = 1
            tempList[-1] = 1
            if None in tempList:
                for n in range(1, i - 1):
                    tempList[n] = rList[i - 2][n - 1] + rList[i - 2][n]
            rList.append(tempList)
        return rList
