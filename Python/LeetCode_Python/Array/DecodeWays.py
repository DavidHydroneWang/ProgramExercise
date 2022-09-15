#!/usr/bin/env python
# coding=utf-8
class Solution: 184 / 269 test cases passed. Status: Wrong Answer
    def numDecodings(self, s: str) -> int:
        #print(ord('Z') - 64)
        decoder = [str(i)  for i in range(1,27)]
        dp = [0] * len(s)
        dp[0] = 1 if s[0] in decoder else 0
        #print(dp)
        for i in range(1, len(s)):
            if s[i] in decoder:
                dp[i] += dp[i - 1]
                dp[i] += 1 if s[i - 1: i + 1] in decoder else 0
            else:
                dp[i] = dp[i - 1]
        #print(dp)
        return dp[-1]


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        if s[0] != '0':
            dp[1] = 1
        for i in range(1, len(s)):
            if s[i] != '0':
                dp[i + 1] += dp[i]
            if 10 <= int(s[i - 1: i + 1]) <= 26:
                dp[i + 1] += dp[i - 1]
        return dp[-1]

class Solution:
    def numDecodings(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        dp = [0] * length
        for index in range(length):
            if index >= 1 and int(s[index - 1:index + 1]) < 27 and int(s[index - 1:index + 1]) >= 10:
                if index == 1:
                    dp[index] = 1
                else:
                    dp[index] += dp[index - 2]
            if int(s[index]) != 0:
                if index == 0:
                    dp[index] = 1
                else:
                    dp[index] += dp[index - 1]
        return dp[-1]


class Solution:
    def numDecodings(self, s: str) -> int:
        length = len(s)
        if length <= 0:
            return 0
        dp = [0] * (length + 1)
        dp[0] = 1
        for i in range(1, length + 1):
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
            if i != 1 and s[i - 2: i] < '27' and s[i -2:i] > '09':
                dp[i] += dp[i - 2]
        return dp[-1]

class Solution:
    def numDecodings(self, s):
        if s[0] == "0": return 0
        dp1 = dp2 = 1
        for i in range(1, len(s)):
            if s[i] == "0" and (s[i - 1] == "0" or s[i - 1] >= "3"): return 0
            dp1, dp2 = [dp2, dp1] if s[i] == "0" else [dp2, dp2 + dp1] if "10" <= s[i -1: i + 1] <= "26" else [dp2, dp2]
        return dp2
