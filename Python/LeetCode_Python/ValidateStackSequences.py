#!/usr/bin/env python
# coding=utf-8
class Solution: # 129 / 151 test cases passed. Status: Wrong Answer
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        while popped[0] != pushed[-1]:
            try:
                pushed.remove(popped[0])
                popped= popped[1:]
            except Exception as e:
                return False

        return pushed == list(reversed(popped))


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j, stack = 0, []
        for v in pushed:
            stack.append(v)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return j == len(pushed)


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        index = 0
        for item in pushed:
            stack.append(item)
            while (stack and stack[-1] == popped[index]):
                stack.pop()
                index += 1

        return len(stack) == 0
