#!/usr/bin/env python
# coding=utf-8
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end = -1
        if not nums:
            return [start, end]
        high, low =  len(nums) -1, 0
        while low < high:
            mid = (high + low) // 2
            if nums[mid] >= target:
                high = mid
            else:
                low = mid + 1
        print(low, high)
        if nums[low] == target:
            start = low
        high, low = len(nums) -1, 0
        while low < high:
            mid = ( low + high) // 2
            if nums[mid] > target:
                high = mid
            else:
                low = mid + 1
        print(low, high)
        if nums[-1] == target:
            end = len(nums) -1
        elif nums[high - 1] == target:
            end = high - 1


        return [start, end]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums: return [-1, -1]
        return [nums.index(target), len(nums) - nums[::-1].index(target) - 1]
