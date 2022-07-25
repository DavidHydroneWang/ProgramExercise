#!/usr/bin/env python
# coding=utf-8


class Solution:
    def isValid(self, s):
        if len(s) % 2 != 0:
            return False
        symbolDic = {'{': '}', '[': ']', '(': ')'}
        stack = []
        for i in range(len(s)):
            if len(stack) == 0:
                if s[i] in symbolDic.keys():
                    stack.append(s[i])
                else:
                    return False
            else:
                if s[i] in symbolDic.keys():
                    stack.append(s[i])
                else:
                    if symbolDic[stack[-1]] == s[i]:
                        stack.pop()
                    else:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False
