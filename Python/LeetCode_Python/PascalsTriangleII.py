#!/usr/bin/env python
# coding=utf-8
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        numRows = rowIndex + 1
        res = [[1] * i for i in range(1, numRows + 1)]
        if numRows == 1:
            return res[rowIndex]
        elif numRows == 2:
            return res[rowIndex]

        for i in range(2, numRows):
            for j in range(1, len(res[i]) - 1):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]


        return res[rowIndex]


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        last = [1]
        res = [1]
        for r in range(1, rowIndex + 1):
            res = [1]
            for index in range(len(last) - 1):
                res.append(last[index] + last[index + 1])
            res.append(1)
            last = res
        return res


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(rowIndex):
            row = [1] + [row[i]+row[i+1] for i in range(len(row)-1)] + [1]
        return row
