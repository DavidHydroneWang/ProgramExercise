#!/usr/bin/env python
# coding=utf-8
from functools import *
class Solution:
    def PrintMinNumber(self , numbers: List[int]) -> str:
        # write code here
        if not numbers:
            return ''

        def compare(s1, s2):
            if s1 + s2 < s2 + s1:
                return -1
            if s1 + s2 > s2 + s1:
                return 1
            return 0

        return ''.join(
            sorted([str(x) for x in numbers], key=cmp_to_key(compare))
        )
