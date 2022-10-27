#!/usr/bin/env python
# coding=utf-8
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 1:
            return min(costs[0])

        r, g, b = 0, 0, 0
        for cost in costs:
            _r, _g, _b = r, g, b
            r = min(_g, _b) + cost[0]
            g = min(_r, _b) + cost[1]
            b = min(_r, _g) + cost[2]

        return min(r, g, b)


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        for i in range(1, len(costs)):
            costs[i][0] += min(costs[i-1][1], costs[i-1][2])
            costs[i][1] += min(costs[i-1][0], costs[i-1][2])
            costs[i][2] += min(costs[i-1][0], costs[i-1][1])

        return min(costs[-1])


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [0] * 3
        for a, b, c in costs:
            c1 = min(dp[1], dp[2]) + a
            c2 = min(dp[0], dp[2]) + b
            c3 = min(dp[0], dp[1]) + c
            dp = [c1, c2, c3]
        return min(dp)
