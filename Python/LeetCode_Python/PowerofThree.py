#!/usr/bin/env python
# coding=utf-8
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        for i in range(n):
            if 3 ** i > n:
                return False
            if not 3 ** i ^ n:
                return True

        return False
