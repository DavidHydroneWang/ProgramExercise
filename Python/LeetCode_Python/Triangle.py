#!/usr/bin/env python
# coding=utf-8
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        index = 0
        #res = triangle[0][0]
        i = 1
        while i < len(triangle):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    minV = min(triangle[i - 1][j - 1 : j + 1])
                    triangle[i][j] +=  minV
            i += 1
        return min(triangle[-1])


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if triangle is None or len(triangle) == 0:
            return 0

        length = len(triangle)
        dp  = [0] * length
        dp[0] = triangle[0][0]
        for i in range(1, length):
            dp[i] = dp[i - 1] + triangle[i][i]
            for j in reversed(range(1, i)):
                dp[j] = min(dp[j - 1] + triangle[i][j], dp[j] + triangle[i][j])
            dp[0] = dp[0] + triangle[i][0]

        return min(dp)


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(len(triangle)-2, -1, -1):

            for col in range(len(triangle[row])):
                triangle[row][col] += min(triangle[row+1][col], triangle[row+1][col+1])

        return triangle[0][0]
