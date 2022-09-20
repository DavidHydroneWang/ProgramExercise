#!/usr/bin/env python
# coding=utf-8
class Solution:
    def grayCode(self, n: int) -> List[int]:

        return [0 ^ i ^ i >> 1 for i in range(1 << n)]


class Solution:
    def grayCode(self, n: int) -> List[int]:
        gray = []
        binary = 0
        while binary < (1 << n):
            gray.append(binary ^ binary >> 1)
            binary += 1
        return gray
