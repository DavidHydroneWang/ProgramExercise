#!/usr/bin/env python
# coding=utf-8
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        stack = []
        while tokens:
            temp = tokens.pop(0)
            if temp not in ['+', '-', '*', '/']:
                stack.append(temp)
            else:
                if temp == '+':
                    i = int(stack.pop())
                    j = int(stack.pop())
                    stack.append(i + j)
                elif temp == '-':
                    i = int(stack.pop())
                    j = int(stack.pop())
                    stack.append(j - i)
                elif temp == '*':
                    i = int(stack.pop())
                    j = int(stack.pop())
                    stack.append(i * j)
                else:
                    i = int(stack.pop())
                    j = int(stack.pop())
                    stack.append( int(j / i))

        return stack[0]
