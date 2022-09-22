#!/usr/bin/env python
# coding=utf-8
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        res = nums1 + nums2
        res.sort()
        if (m + n) % 2 == 0:
            return (res[(m + n)// 2 - 1] + res[(m + n)// 2 ]) / 2
        else:
            return  res[(m + n)// 2 ] * 2/ 2
