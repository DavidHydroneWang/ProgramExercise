#!/usr/bin/env python
# coding=utf-8
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        for i in range(1, x//2 + 1):
            if  i *  i <=  x  and (i + 1) *  (i + 1) > x:
                return i


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        guess = x
        while guess * guess > x:
            guess = (guess + x // guess) // 2
        return guess

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                l = mid + 1
            else:
                r = mid - 1
        return l - 1
