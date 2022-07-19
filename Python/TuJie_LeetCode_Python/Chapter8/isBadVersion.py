#!/usr/bin/env python
# coding=utf-8


class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n
        while left < n:
            mid = (left + right) // 2
            if isBadVersion(mid):
                if isBadVersion(mid - 1):
                    right = mid
                else:
                    return mid
            else:
                if isBadVersion(mid + 1):
                    return mid + 1
                else:
                    left = mid
