#!/usr/bin/env python
# coding=utf-8
class Solution:  # 210 / 311 test cases passed
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        from itertools import combinations as cb
        res = []
        if len(nums) < 3:
            return res
        visited = []
        for i, j, k in cb(nums, 3):
            temp = [i, j, k]
            temp.sort()
            if temp not in visited:
                visited.append(temp)
                if i + j + k == 0:
                    res.append([i, j, k])

        return res


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res, res_set = [], set()
        nums.sort()
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                sm = nums[i] + nums[l] + nums[r]
                if sm < 0: l += 1
                elif sm > 0: r -= 1
                elif (nums[i], nums[l], nums[r]) not in res_set:
                    res.append([nums[i], nums[l], nums[r]])
                    res_set.add((nums[i], nums[l], nums[r]))
                else: l, r = l + 1, r - 1
        return res


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                if currentSum < 0:
                    left += 1
                elif currentSum > 0:
                    right -= 1
                else:
                    result.append((nums[i], nums[left], nums[right]))
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result
