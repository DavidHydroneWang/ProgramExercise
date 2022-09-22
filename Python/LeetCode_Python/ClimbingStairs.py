#!/usr/bin/env python
# coding=utf-8
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        stairs, prev = 2, 1
        for _ in range(3, n + 1):
            stairs, prev = stairs + prev, stairs

        return stairs


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(i):
            if i >= n: return 1 if i == n else 0
            if i not in memo:
                memo[i] = dfs(i + 1) + dfs(i + 2)
            return memo[i]
        return dfs(0)
