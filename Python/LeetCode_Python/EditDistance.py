#!/usr/bin/env python
# coding=utf-8
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if not (i and j):
                    dp[i][j] = i or j
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] += dp[i -1 ][j - 1]
                else:
                    dp[i][j] += min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[-1][-1]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        # dp[i][j] := min # of operations to convert word1[0..i) to word2[0..j)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][0] = i

        for j in range(1, n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[m][n]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def edit_distance(i, j):
            if i < 0 or j < 0:
                return i + 1 + j + 1

            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                result = edit_distance(i - 1, j - 1)
            else:
                result = 1 + min(edit_distance(i - 1, j),
                                 edit_distance(i, j - 1),
                                 edit_distance(i - 1, j - 1))

            memo[(i, j)] = result
            return result

        memo = {}
        return edit_distance(len(word1) - 1, len(word2) - 1)
