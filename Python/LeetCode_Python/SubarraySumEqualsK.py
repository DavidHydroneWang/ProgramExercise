#!/usr/bin/env python
# coding=utf-8
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_dic = {0:1}
        pre_sum = 0
        count = 0

        for num in nums:
            pre_sum += num
            if pre_sum - k in pre_dic:
                count += pre_dic[pre_sum - k]
            if pre_sum in pre_dic:
                pre_dic[pre_sum] += 1
            else:
                pre_dic[pre_sum] = 1
            #print(pre_dic)

        return count
