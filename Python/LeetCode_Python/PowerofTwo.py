#!/usr/bin/env python
# coding=utf-8
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(n):
            if 2 ** i > n:
                return False
            if 2 ** i == n:
                return True

        return False


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i  in range(32):
            if 2 ** i ^ n == 0:
                return True

        return False
