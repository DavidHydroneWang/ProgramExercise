#!/usr/bin/env python
# coding=utf-8


class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        mins = prices[0]
        maxes = 0
        for i in range(1, len(prices)):
            mins = min(prices[i], mins)
            maxes = max(prices[i] - mins, maxes)

        return maxes


class Solution:
    def maxProfit(self, prices):
        sums = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                sums += prices[i + 1] - prices[i]
        return sums
