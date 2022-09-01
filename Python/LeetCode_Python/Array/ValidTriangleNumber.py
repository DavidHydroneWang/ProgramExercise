#!/usr/bin/env python
# coding=utf-8
class Solution: # 223 / 241 test cases passed.
    def triangleNumber(self, nums: List[int]) -> int:
        from itertools import combinations as cb
        res = 0
        for i, j, k in cb(nums, 3):
            #print(i, j, k)
            if i + j > k and abs(i - j) < k:
                res += 1

        return res


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res, n = 0, len(nums)
        nums.sort()
        for i in range(n - 1, 1, -1):
            j, k = i - 1, 0
            while k < j:
                if nums[j] + nums[k] > nums[i]:
                    res, j = res + j - k, j - 1
                else:
                    k += 1
        return res
