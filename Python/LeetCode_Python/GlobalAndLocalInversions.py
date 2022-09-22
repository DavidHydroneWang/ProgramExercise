#!/usr/bin/env python
# coding=utf-8
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        res = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    if i == j - 1:
                        res.append(True)
                    else:
                        return False
        return all(res)A


class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        for i, num in enumerate(nums):
            if not (i - 1 <= num <= i + 1):
                return False
        return True


class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if abs(nums[i]  - i) > 1:
                return False
        return True
