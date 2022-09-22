#!/usr/bin/env python
# coding=utf-8
class Solution: #  259 / 283 test cases passed. Time Limit Exceeded
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 0 or n == 1:
            return 0
        if n == 2:
            return min(cost)
        return min(self.minCostClimbingStairs(cost[:-1]) + cost[-1] ,self.minCostClimbingStairs(cost[:-2]) + cost[-2])


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev, step = cost[:2]

        for c in cost[2:]:
            prev, step = step, min(prev, step) + c

        return min(prev, step)


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2,len(cost)):
            cost[i] += min(cost[i-1],cost[i-2])
        return min(cost[-1],cost[-2])
