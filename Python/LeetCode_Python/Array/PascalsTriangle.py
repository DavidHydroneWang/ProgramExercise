#!/usr/bin/env python
# coding=utf-8

class Solution: # time limit exceeded
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1] * i for i in range(1, numRows + 1)]
        if numRows == 1:
            return res
        elif numRows == 2:
            return res

        for i in range(2, numRows + 1):
            for j in range(1, len(res[i - 1]) - 1):
                res[i - 1][j] = self.generate(i - 1)[i - 2][j - 1] + self.generate(i - 1)[i - 2][j]


        return res

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1] * i for i in range(1, numRows + 1)]
        if numRows == 1:
            return res
        elif numRows == 2:
            return res

        for i in range(2, numRows):
            for j in range(1, len(res[i]) - 1):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]


        return res



class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            result.append([0] * (i + 1))
        for i in range(numRows):
            for j in range(i + 1):
                if j == 0 or j == i:
                    result[i][j] = 1
                else:
                    result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
        return result
