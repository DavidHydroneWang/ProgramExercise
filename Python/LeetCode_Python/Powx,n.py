#!/usr/bin/env python
# coding=utf-8
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x
        half = self.myPow(x, n // 2)
        return half * half * self.myPow(x, n % 2)


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
             return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)
