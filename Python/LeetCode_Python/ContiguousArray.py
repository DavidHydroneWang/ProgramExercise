#!/usr/bin/env python
# coding=utf-8
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pre_dic = {0: -1}
        count = 0
        pre_sum = 0
        for i in range(len(nums)):
            if nums[i]:
                pre_sum += 1
            else:
                pre_sum -= 1
            if pre_sum in pre_dic:
                count = max(count, i - pre_dic[pre_sum])
            else:
                pre_dic[pre_sum] = i
        return count


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        s = 0
        dic = {0: -1}
        for i, v in enumerate(nums):
            s += 1 if v == 1 else -1
            if s in dic:
                res = max(res, i - dic[s])
            else:
                dic[s] = i

        return res
