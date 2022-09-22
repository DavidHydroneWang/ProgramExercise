#!/usr/bin/env python
# coding=utf-8
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for i in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m-1][n-1]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                x = path[i - 1][j] if i - 1 >= 0 else 0
                y = path[i][j - 1] if j - 1 >= 0 else 0
                if x + y == 0:
                    path[i][j] = 1
                else:
                    path[i][j] = x + y

        return path[n - 1][m - 1]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1
        for i in range(n):
            for j in range(m):
                if i - 1 >= 0:
                    dp[i][j] += dp[i - 1][j]
                if j - 1 >= 0:
                    dp[i][j] += dp[i][j - 1]
        return dp[-1][-1]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0

        row_paths = [1 for _ in range(n)]       # first row, one path to each column

        for row in range(m-1):
            new_row_paths = [1]                 # one path to first col of each row
            for col in range(1, n):
                new_row_paths.append(new_row_paths[-1] + row_paths[col])
            row_paths = new_row_paths

        return row_paths[-1]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0
        dp = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i][j - 1] +  dp[i - 1][j]
        return dp[-1][-1]
