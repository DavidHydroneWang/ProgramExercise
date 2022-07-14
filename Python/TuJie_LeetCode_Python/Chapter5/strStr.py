#!/usr/bin/env python
# coding=utf-8


class Solution:
    def strStr(self, haystack: str, neddle: str) -> int:
        if len(neddle) > len(haystack):
            return -1
        if neddle == haystack:
            return 0
        length = len(neddle)
        pointer = 0
        while pointer <= (len(haystack) - len(neddle)):
            if haystack[pointer: pointer + length] == neddle:
                return pointer
            else:
                pointer += 1
        return -1
