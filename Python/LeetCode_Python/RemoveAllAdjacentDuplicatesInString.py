#!/usr/bin/env python
# coding=utf-8
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        #stack.append(s[0])
        #res = 0
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if i != stack[-1]:
                    stack.append(i)
                else:
                    stack.pop()
                    #res += 1
        #print(res)
        return "".join(stack)



class Solution:
    def removeDuplicates(self, s: str) -> str:
        i = 0
        while True:
            if i + 1 > len(s) - 1:
                break
            if s[i] == s[i+1]:
                s = s[:i] + s[i+2:]
                i = max(i-1, 0)
            else:
                i += 1
        return s


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
