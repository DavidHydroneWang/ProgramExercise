#!/usr/bin/env python
# coding=utf-8
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        n = len(grid)
        m = len(grid[0])
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == '0':
            return 0
        grid[i][j] = '0'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res, n, m = 0, len(grid), len(grid[0]) if grid else 0
        def explore(i, j):
            grid[i][j] = "-1"
            if i > 0 and grid[i - 1][j] == "1": explore(i - 1, j)
            if j > 0 and grid[i][j - 1] == "1": explore(i, j - 1)
            if i + 1 < n and grid[i + 1][j] == "1": explore(i + 1, j)
            if j + 1 < m and grid[i][j + 1] == "1": explore(i, j + 1)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1": explore(i, j); res += 1
        return res
