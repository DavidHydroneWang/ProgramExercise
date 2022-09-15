#!/usr/bin/env python
# coding=utf-8
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length == 0:
            return 0
        max_profit, low = 0, prices[0]
        for i in range(1, length):
            if low > prices[i]:
                low = prices[i]
            else:
                temp = prices[i] - low
                if temp > max_profit:
                    max_profit = temp
        return max_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = float('inf'), 0
        for price in prices:
            buy = min(buy, price)
            sell = max(sell, price - buy)

        return sell
