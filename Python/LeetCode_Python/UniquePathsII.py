#!/usr/bin/env python
# coding=utf-8
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        if not m or not n:
            return 0
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1 if not obstacleGrid[0][0] else 0

        for i in range( n):
            for j in range( m):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    if obstacleGrid[i][j]:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    if obstacleGrid[i][j]:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i - 1][j]
                else:
                    if obstacleGrid[i][j]:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i][j - 1] +  dp[i - 1][j]

        return dp[-1][-1]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]

        return dp[n - 1]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # dp[i][j] := unique paths from (0, 0) to (i - 1, j - 1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][1] = 1  # can also set dp[1][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if obstacleGrid[i - 1][j - 1] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m][n]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if not m or not n:
            return 0
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0

        row_paths = [0 for _ in range(n+1)]
        row_paths[1] = 1

        for row in range(1, m+1):
            new_row_paths = [0]
            for col in range(1, n+1):
                if obstacleGrid[row-1][col-1]:
                    new_row_paths.append(0)
                else:
                    new_row_paths.append(new_row_paths[-1] + row_paths[col])
            row_paths = new_row_paths

        return row_paths[-1]
