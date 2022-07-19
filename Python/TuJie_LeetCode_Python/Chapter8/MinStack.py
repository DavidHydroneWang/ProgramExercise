#!/usr/bin/env python
# coding=utf-8


class Solution:
    def __init(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        try:
            self.stack.pop()
        except Exception as e:
            pass

    def top(self):
        try:
            x = self.stack[-1]
        except Exception as e:
            return None
        else:
            return x

    def getMin(self):
        try:
            mi = min(self.stack)
        except Exception as e:
            return None
        else:
            return mi
