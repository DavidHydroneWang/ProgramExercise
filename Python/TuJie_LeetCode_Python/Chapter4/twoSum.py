#!/usr/bin/env python
# coding=utf-8


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            for j  in range(len(nums) - 1):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            if target - nums[i] in nums[i + 1:]:
                j = nums[i + 1:].index(target - nums[i])
                return [i, i + j + 1]
