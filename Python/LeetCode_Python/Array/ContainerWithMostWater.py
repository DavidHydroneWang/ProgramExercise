#!/usr/bin/env python
# coding=utf-8


class Solution:
    def maxArea(self, height):
        l, r = 0, len(height - 1)
        currentMax = 0
        while l != r:
            currentMax = max(min(height[r], height[l]) * (r - l), currentMax)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return currentMax
