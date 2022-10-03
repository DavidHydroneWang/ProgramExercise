#!/usr/bin/env python
# coding=utf-8
class Solution:
    def movingCount(self , threshold: int, rows: int, cols: int) -> int:
        # write code here
        def dfs(i, j):
            if ( i >= rows or j >= cols or vis[i][j] or (i % 10 + int(i /10) + j % 10 + int(j / 10)) > threshold):
                return 0
            vis[i][j] = True
            return 1 + dfs(i + 1, j) + dfs(i, j + 1)

        vis = [[False] * cols for _ in range(rows)]
        return dfs(0, 0)
