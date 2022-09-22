#!/usr/bin/env python
# coding=utf-8
class Solution:
    def canWinNim(self, n: int) -> bool:
        if n < 4:
            return True
        if n % 4 == 0:
            return False
        return  (n - 1) % 4 == 0 or (n - 2) % 4 == 0 or (n - 3) % 4 == 0


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
