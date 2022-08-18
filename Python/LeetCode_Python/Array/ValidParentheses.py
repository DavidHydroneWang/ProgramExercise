#!/usr/bin/env python
# coding=utf-8
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            elif i == ')':
                if stack:
                    temp = stack.pop()
                    if temp == '(':
                        continue
                    else:
                        return False
                else:
                    return False
            elif i == ']':
                if stack:
                    temp = stack.pop()
                    if temp == '[':
                        continue
                    else:
                        return False
                else:
                    return False
            elif i == '}':
                if stack:
                    temp = stack.pop()
                    if temp == '{':
                        continue
                    else:
                        return False
                else:
                    return False
        return stack == []


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {'(' : ')', '[' : ']', '{' : '}'}

        for c in s:
            if c in match:
                stack.append(c)
            else:
                if not stack or match[stack.pop()] != c:
                    return False

        return not stack
