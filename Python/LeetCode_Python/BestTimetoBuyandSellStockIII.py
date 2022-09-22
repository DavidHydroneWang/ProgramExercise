#!/usr/bin/env python
# coding=utf-8
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1, buy2 = float('-inf'), float('-inf')
        sell1, sell2 = 0, 0

        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, price + buy1)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, price + buy2)

        return sell2


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.maxProfitWithKTransaction(prices, 2)


    def maxProfitWithKTransaction(self, prices, k):
        if not prices:
            return 0
        profits = [[0 for d in prices] for t in range(k + 1)]
        for t in range(1, k + 1):
            maxThusFar = float('-inf')
            for d in range(1, len(prices)):
                maxThusFar = max(maxThusFar, profits[t - 1][d - 1] - prices[d - 1])
                profits[t][d] = max(profits[t][d - 1], maxThusFar + prices[d])
        return profits[-1][-1]
