#!/usr/bin/env python
# coding=utf-8
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        max_len = 0
        directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}

        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        record  = [[0] * cols for _ in range(rows)]

        def dfs(i, j):
            nonlocal max_len
            record[i][j] = 1
            for direction in directions:
                new_i, new_j = i + direction[0], j + direction[1]
                if 0 <= new_i < rows and 0 <= new_j < cols and matrix[new_i][new_j] > matrix[i][j]:
                    if record[new_i][new_j] == 0:
                        dfs(new_i, new_j)
                    record[i][j] = max(record[i][j], record[new_i][new_j] + 1)
            max_len = max(max_len, record[i][j])

        for i in range(rows):
            for j in range(cols):
                if record[i][j] == 0:
                    dfs(i, j)

        return max_len


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        self.res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.dfs(i, j, 1)
        return self.res

    @lru_cache(None)
    def dfs(self, i, j, count):
        self.res = max(self.res, count)
        if i-1 >= 0 and self.matrix[i-1][j] > self.matrix[i][j]:
            self.dfs(i-1, j, count+1)
        if j-1 >= 0 and self.matrix[i][j-1] > self.matrix[i][j]:
            self.dfs(i, j-1, count+1)
        if i+1 < len(self.matrix) and self.matrix[i+1][j] > self.matrix[i][j]:
            self.dfs(i+1, j, count+1)
        if j+1 < len(self.matrix[0]) and self.matrix[i][j+1] > self.matrix[i][j]:
            self.dfs(i, j+1, count+1)


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        @functools.lru_cache(None)
        def dfs(i: int, j: int, prev: int) -> int:
            if i < 0 or i == m or j < 0 or j == n:
                return 0
            if matrix[i][j] <= prev:
                return 0

            curr = matrix[i][j]
            return 1 + max(dfs(i + 1, j, curr),
                         dfs(i - 1, j, curr),
                         dfs(i, j + 1, curr),
                         dfs(i, j - 1, curr))

        return max(dfs(i, j, -math.inf) for i in range(m) for j in range(n))
