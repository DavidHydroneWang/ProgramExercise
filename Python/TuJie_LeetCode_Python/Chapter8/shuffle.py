#!/usr/bin/env python
# coding=utf-8


class Solution:
    def __init(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        import random
        sList = self.nums[:]
        rList = []
        while sList:
            val = random.choice(sList)
            rList.append(val)
            sList.remove(val)
        return rList
