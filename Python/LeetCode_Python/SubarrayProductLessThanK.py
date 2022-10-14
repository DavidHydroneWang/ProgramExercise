#!/usr/bin/env python
# coding=utf-8
class Solution:  # 76 / 97 test cases passed. Status: Time Limit Exceeded
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            product = nums[i]
            if product < k:
                res += 1
                right = i + 1
                while right < len(nums):
                    if nums[right] == 1:
                        res += 1
                        right += 1
                    else:
                        product *=  nums[right]
                        if product < k:
                            res += 1
                            right += 1
                        else:
                            break
        return res


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        pro = 1
        left, right =  0, 0
        while right < len(nums):
            pro *= nums[right]
            right += 1
            while pro >= k and left < right:
                pro /= nums[left]
                left += 1
            res += right - left


        return res


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        size = len(nums)
        left = 0
        right = 0
        window_product = 1

        count = 0

        while right < size:
            window_product *= nums[right]

            while window_product >= k:
                window_product /= nums[left]
                left += 1

            count += (right - left + 1)
            right += 1

        return count
