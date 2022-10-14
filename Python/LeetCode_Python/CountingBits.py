#!/usr/bin/env python
# coding=utf-8
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            res.append(bin(i).count('1'))

        return res


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [ 0 for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i] = dp[i & (i - 1)] + 1
        return dp


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [ 0 for _ in range(n + 1)]

        for i in range(1, n + 1):
            if i % 2 == 1:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i // 2]
        return dp


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            # res[left:last] + last bit
            res[i] = res[i >> 1] + (i & 1)
        return res
