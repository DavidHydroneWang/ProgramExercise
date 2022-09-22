#!/usr/bin/env python
# coding=utf-8
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(list(set(nums)))
