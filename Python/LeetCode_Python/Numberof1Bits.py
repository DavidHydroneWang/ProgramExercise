#!/usr/bin/env python
# coding=utf-8
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += (n & 1)
            n = n >> 1
        return ans


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n &= n - 1
            ans += 1
        return ans


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
