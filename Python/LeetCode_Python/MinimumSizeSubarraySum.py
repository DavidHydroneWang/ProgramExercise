#!/usr/bin/env python
# coding=utf-8
class Solution: #  18 / 20 test cases passed. Status: Time Limit Exceeded
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')

        for i in range(len(nums)):
            #print(nums[i])
            right = i + 1
            while right <= len(nums) :
                curr = sum(nums[i:right])
                #print(curr)
                if curr >= target:
                    if res > right - i :
                        res = right - i
                    break

                else:
                    right += 1
        if res == float('inf'):
            return 0
        return res


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        sum = 0
        left, right = 0, 0
        while right < len(nums):
            sum += nums[right]
            right += 1
            while sum >= target:
                res = min(res, right - left)
                sum -= nums[left]
                left += 1
        if res == float('inf'):
            return 0
        return res


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        summ = 0
        left =  0
        for right, num in enumerate(nums):
            summ += num
            while summ >= target:
                res = min(res, right - left + 1)
                summ -= nums[left]
                left += 1
        if res == float('inf'):
            return 0
        return res
