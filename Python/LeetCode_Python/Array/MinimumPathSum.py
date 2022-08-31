#!/usr/bin/env python
# coding=utf-8
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[float('inf') for _ in range(len(grid[0]) + 1)] for _ in range(len(grid) + 1)]
        for i in range(1, len(grid) + 1):
            for j in range(1, len(grid[0]) + 1):
                minNum = min(dp[i - 1][j], dp[i][j - 1])
                if (dp[i - 1][j] == float('inf') and dp[i][j - 1] == float('inf')):
                    minNum = 0
                dp[i][j] = minNum + grid[i - 1][j - 1]
        return dp[-1][-1]



class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        min_path = [float('inf') for _ in range(n + 1)]
        min_path[1] = 0

        for row in range(1, m + 1):
            new_min_path = [float('inf') for _ in range(n + 1)]
            for col in range(1, n + 1):
                new_min_path[col] = grid[row - 1][col - 1] + min(min_path[col], new_min_path[col - 1])
            min_path = new_min_path

        return min_path[-1]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] += min(grid[i][j - 1] if j > 0 else float("inf"), grid[i - 1][j] if i > 0 else float("inf")) if i!=0 or j != 0 else 0
        return grid[-1][-1]
