#!/usr/bin/env python
# coding=utf-8
class Solution:  16 / 21 test cases passed. Time Limit Exceeded
    def removeDuplicates(self, s: str, k: int) -> str:
        i = 0
        flag = True
        while True:
            if i + k - 1 > len(s) - 1:
                break

            for j in range(1, k):
                if s[i + j] != s[i]:
                    flag = False

            if flag:
                s = s[:i] + s[i + k:]
                i = max(0, i - k + 1)
            else:
                i += 1
                flag = True

        return s


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for i, c in enumerate(s):
            if not stack or stack[-1][0] !=c:
                stack.append([c, 1])
            else:
                stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()

        return ''.join(k * v for k, v in stack)
