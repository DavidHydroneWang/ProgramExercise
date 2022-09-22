#!/usr/bin/env python
# coding=utf-8
class Solution: # time limit exceeded
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        largest = nums[-1]
        if largest > 0:
            for i in range(1, largest):
                if i not in nums:
                    return i
        else:
            return 1

        return largest + 1


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = 1
        for num in sorted(nums):
            res += num == res
        return res


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1
        nums = sorted(nums)
        length = len(nums) -1
        index = 0
        for i, n in enumerate(nums):
            if n >= 0:
                index = i
                break
        d = nums[index]
        if d > 1: return 1
        for i, n in enumerate(nums[index + 1:]):
            if d + 1 == n or d == n:
                d = n
            else: break
        return d + 1 if d + 1 > 0 else 1
