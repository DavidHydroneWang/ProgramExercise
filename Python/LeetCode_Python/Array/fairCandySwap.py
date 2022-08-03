#!/usr/bin/env python
# coding=utf-8


class Solution:
    def fairCandySwap(self, A, B):
        x = (sum(A) - sum(B)) // 2
        b = set(B)
        for i in A:
            if i - x in b:
                return (i, i - x)
