#!/usr/bin/env python
# coding=utf-8
class Solution:
    def hasPath(self , matrix: List[List[str]], word: str) -> bool:
        # write code here
        def dfs(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or word[k] != matrix[i][j]:
                return False
            matrix[i][j] = ''
            ans = any(dfs(i + a, j + b, k + 1) for a, b in [[0, -1], [0, 1], [1, 0], [-1, 0]])
            matrix[i][j] = word[k]
            return ans

        m, n = len(matrix), len(matrix[0])
        return any(dfs(i, j, 0) for i in range(m) for j in range(n))
