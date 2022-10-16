#!/usr/bin/env python
# coding=utf-8
class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)

        dp = [[False for _ in range(length)] for _ in range(length)]
        subStringCount = 0

        for i in range(length):
            dp[i][i] = 1
            subStringCount += 1

        for start in range(length - 1, -1, -1):
            for end  in range(start + 1, length):
                if s[start] == s[end]:
                    if end - start == 1 or dp[start + 1][end - 1]:
                        dp[start][end] = True
                        subStringCount += 1

        return subStringCount


class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        dp = [[False for _ in range(size)] for _ in range(size)]
        res = 0
        for i in range(size - 1, -1, -1):
            for j in range(i, size):
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False
                if dp[i][j]:
                    res += 1
        return res
