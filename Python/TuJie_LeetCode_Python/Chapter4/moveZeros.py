#!/usr/bin/env python
# coding=utf-8


class Solution:
    def moveZeros(self, nums):
        """
        :type nums: List[int]
        :rtype: void
        """
        left = 0
        right = 0
        while right < len(nums) - 1:
            if nums[left] == 0:
                nums[left: -1] = nums[left + 1:]
                nums[-1] = 0
                right += 1
            else:
                left += 1
                right += 1
        return


class Solution:
    def moveZeros(self, nums):
        """
        :type nums: List[int]
        :rtype: void
        """
        for n in nums:
            if n == 0:
                nums.remove(0)
                nums.append(0)
        return
