#!/usr/bin/env python
# coding=utf-8
class Solution: # 156 / 231
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        res = []
        temp = 0
        #match = {'(' : ')'}
        for i in s:
            if i == '(':
                stack.append(i)
            else:
                if stack and stack.pop() == '(':
                    temp += 2
                    res.append(temp)
                else:
                    res.append(temp)
                    temp = 0
        if not res:
            return 0
        return max(res)


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []                  # indices of brackets that are not matched

        for i, c in enumerate(s):
            if c == ")" and stack and s[stack[-1]] == '(':
                stack.pop()         # close matches an open on the stack
            else:
                stack.append(i)     # puch open brackets or unmatched close brackets

        stack.append(len(s))        # last unmatched index after end of s
        max_length = stack[0]       # first unmatched index before start of s

        for index in range(1, len(stack)):  # find max gap between remaining unmatched indices
            max_length = max(max_length, stack[index] - stack[index-1] - 1)

        return max_length
