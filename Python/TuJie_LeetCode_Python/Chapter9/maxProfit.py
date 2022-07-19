#!/usr/bin/env python
# coding=utf-8


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        maxList = []
        for j in range(len(prices) - 1):
            for i in range(j + 1, len(prices)):
                maxList.append(prices[i] - prices[j])
        profit = max(maxList)
        if profit < 0:
            return 9
        else:
            return profit


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices) - 1):
            sub = max(prices[i + 1:]) - prices[i]
            profit = max(sub, profit)
        return profit
