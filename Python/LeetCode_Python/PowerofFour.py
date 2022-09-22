#!/usr/bin/env python
# coding=utf-8
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        for i in range(n):
            if 4 ** i > n:
                return False
            if not 4 ** i ^ n:
                return True

        return False


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n-1)) == 0 and (n-1) % 3 == 0
