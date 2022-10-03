#!/usr/bin/env python
# coding=utf-8
class Solution:
    def cutRope(self , n: int) -> int:
        # write code here
        if n < 4:
            return n - 1
        ans = 1
        while n > 4:
            ans *= 3
            n -= 3
        ans *= n
        return ans
