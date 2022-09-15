#!/usr/bin/env python
# coding=utf-8
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sums = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                sums += prices[i + 1] - prices[i]

        return sums


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # stock, no stock
        dp = [-float('inf'), 0]
        for p in prices:
            x = max(dp[1] - p, dp[0])
            y = max(dp[1], dp[0] + p)
            dp = [x, y]
        return dp[-1]
