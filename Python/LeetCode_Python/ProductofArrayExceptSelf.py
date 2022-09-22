#!/usr/bin/env python
# coding=utf-8
class Solution:#  18 / 22 test cases passed. Status: Time Limit Exceeded
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i in range(len(nums)):
            temp = nums[:]
            temp.remove(nums[i])

            if 0 in temp:
                pass
            else:
                res[i] = self.product(temp)

        return res

    def product(self, nums):
        res = 1
        for i in nums:
            res *= i
        return res


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [0] * length
        right = [0] * length
        left[0] = 1
        right[length - 1] = 1

        for i in range(1, length):
            left[i] = left[i -1 ] * nums[i - 1]
            right[length - i - 1 ] =  right[length -  i] * nums[length - i]
        #print(left, right)
        for i in range(length):
            left[i] *= right[i]

        return left
