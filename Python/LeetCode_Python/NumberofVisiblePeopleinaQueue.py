#!/usr/bin/env python
# coding=utf-8
class Solution: # 31 / 42 test cases passed. Status: Time Limit Exceeded
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = [0] * len(heights)

        for i in range(len(heights)):
            res = 0
            for j in range(i + 1, len(heights)):
                if heights[i] > heights[j]:
                    ans[i] += 1
                    if j != i + 1 and heights[j] <= max(heights[i + 1: j]):
                        ans[i] -= 1
                elif heights[i] <= heights[j]:
                    ans[i] += 1
                    break
        return ans


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = [0] * len(heights)
        stack = []
        for i in range(len(heights) - 1, -1, -1):
            #print(stack)
            while stack:
                ans[i] += 1
                if heights[i] > stack[-1]:
                    stack.pop()
                else:
                    break
            stack.append(heights[i])


        return ans


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = [0] * len(heights)
        stack = []

        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] <= height:
                ans[stack.pop()] += 1
            if stack:
                ans[stack[-1]] += 1
            stack.append(i)

        return ans
