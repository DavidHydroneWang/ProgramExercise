#!/usr/bin/env python
# coding=utf-8
class Solution:
    def LCS(self , s1: str, s2: str) -> str:
        # write code here
        if s1 == None or s2 == None:
            return '-1'
        m, n = len(s1), len(s2)
        last = [''] * (n + 1)
        for i in range(m):
            cur = [''] * (n + 1)
            for j in range(n):
                if s1[i] == s2[j]:
                    cur[j + 1] = last[j] + s1[i]
                else:
                    cur[j + 1] = cur[j] if(len(cur[j]) >= len(last[j + 1])) else last[j + 1]
            last[:] = cur
        return last[-1] if len(last[-1]) > 0 else '-1'
