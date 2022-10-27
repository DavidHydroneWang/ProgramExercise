#!/usr/bin/env python
# coding=utf-8
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)
        dp = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range( i + 1, n):
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

        def dfs(s, i, t):
            nonlocal n
            if i == n:
                ans.append(t.copy())
                return

            for j in range(i, n):
                if dp[i][j]:
                    t.append(s[i: j + 1])
                    dfs(s, j + 1, t)
                    t.pop()
        dfs(s, 0, [])
        return ans


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def isPalindrome(s: str) -> bool:
            return s == s[::-1]

        def dfs(s: str, j: int, path: List[str]) -> None:
            if j == len(s):
                ans.append(path)
                return

            for i in range(j, len(s)):
                if isPalindrome(s[j: i + 1]):
                    dfs(s, i + 1, path + [s[j: i + 1]])

        dfs(s, 0, [])
        return ans


class Solution:
    res = []
    path = []
    def backtrack(self, s: str, start_index: int):
        if start_index >= len(s):
            self.res.append(self.path[:])
            return
        for i in range(start_index, len(s)):
            if self.ispalindrome(s, start_index, i):
                self.path.append(s[start_index: i+1])
                self.backtrack(s, i + 1)
                self.path.pop()

    def ispalindrome(self, s: str, start: int, end: int):
        i, j = start, end
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        self.res.clear()
        self.path.clear()
        self.backtrack(s, 0)
        return self.res
