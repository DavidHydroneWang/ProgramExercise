#!/usr/bin/env python
# coding=utf-8
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        stack = []
        for i in nums:
            #print(i)
            if not i in stack:
                stack.append(i)
            else:
                stack.remove(i)
        return stack[0]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for i in nums[1:]:
            res ^= i
        return res
