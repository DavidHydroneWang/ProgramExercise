#!/usr/bin/env python
# coding=utf-8


class Solution:
    def maxProfit(self, prices):
        """
        type prices: List[int]
        rtype: int
        """
        maxPro = 0
        i = 1
        while i < len(prices):
            profit = prices[i] - prices[i - 1]
            if profit > 0:
                maxPro += profit
            i += 1
        return maxPro
