#!/usr/bin/env python
# coding=utf-8
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minV = 1
        maxV = max(piles)

        while minV < maxV:
            mid = (minV + maxV) >> 1
            if  self.helper(piles, mid) > h:
                minV = mid + 1
            else:
                maxV = mid
        return minV

    def helper(self, piles, mid):
        res = 0
        for i in piles:
            if i % mid == 0:
                res += int(i/mid)
            else:
                res += int(i/mid) + 1
        return res



class Solution:

    def canEat(self, piles, hour, speed):
        time = 0
        for pile in piles:
            time += (pile + speed - 1) // speed
        return time <= hour

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left) // 2
            if not self.canEat(piles, h, mid):
                left = mid + 1
            else:
                right = mid

        return left


class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) >> 1
            s = sum((pile + mid - 1) // mid for pile in piles)
            if s <= h:
                right = mid
            else:
                left = mid + 1
        return left
