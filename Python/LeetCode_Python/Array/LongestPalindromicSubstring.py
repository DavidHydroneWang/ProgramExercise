#!/usr/bin/env python
# coding=utf-8
class Solution: # 127 / 140 test cases passed. Time Limit Exceeded
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length == 1:
            return s
        if length == 2:
            if s == s[::-1]:
                return s
            else:
                return s[0]
        palindrome = ''
        palindrome_length = 0
        for i in range(length):
            j = i + 1
            while j < length + 1:
                if self.isPalindrome(s[i:j]) and palindrome_length < len(s[i:j]):
                    palindrome = s[i:j]
                    palindrome_length = len(s[i:j])
                    if palindrome_length == length:
                        return palindrome

                j += 1
        return palindrome

    def isPalindrome(self, s):
        return s == s[::-1]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        dp = [[False for _ in range(n)] for _ in range(n)]
        max_start = 0
        max_len = 1

        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and (j - i + 1) > max_len:
                    max_len = j - i + 1
                    max_start = i
        return s[max_start: max_start+max_len]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        maxlenth = 0
        left = 0
        right = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[j] == s[i]:
                    if j - i <= 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                if dp[i][j] and j - i + 1 > maxlenth:
                    maxlenth = j - i + 1
                    left = i
                    right = j
        return s[left:right + 1]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def find_point(i, j, s):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return i + 1, j

        def compare(start, end, left, right):
            if right - left > end - start:
                return left, right
            else:
                return start, end

        start = 0
        end = 0
        for i in range(len(s)):
            left, right = find_point(i, i, s)
            start, end = compare(start, end, left, right)

            left, right = find_point(i, i + 1, s)
            start, end = compare(start, end, left, right)
        return s[start:end]
