#!/usr/bin/env python
# coding=utf-8

class Solution: # 47 / 60 test cases passed.  Time Limit Exceeded
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        dp = [[0] * n for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(n):
                if i != j:
                    dp[i][j] = min(height[i], height[j]) * abs(i - j)
                    if res < dp[i][j]:
                        res = dp[i][j]

        return res


class Solution:
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        currentMax = 0
        while l != r:
            currentMax = max(min(height[r], height[l]) * (r - l), currentMax)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return currentMax
