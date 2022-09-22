#!/usr/bin/env python
# coding=utf-8
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k >= len(prices) // 2:
            return sum(sell - buy for sell, buy in zip(prices[1:], prices[:-1]) if sell - buy > 0)
        dp = [[0, -float("inf")] for _ in range(k + 1)]
        for p in prices:
            for i in range(k + 1):
                if i and dp[i - 1][1] + p > dp[i][0]:
                    dp[i][0] = dp[i - 1][1] + p
                if dp[i][0] - p > dp[i][1]:
                    dp[i][1] = dp[i][0] - p
        return dp[-1][0]


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k >= len(prices) // 2:       # can transact as often as required to get max profit
            return sum([max(0, prices[i] - prices[i-1]) for i in range(1, len(prices))])

        # buys[i] is the max profit after i-1 buy/sell transactions and another buy
        # sells[i] is the max profit after i buy/sell transactions
        buys, sells = [float('-inf') for _ in range(k + 1)], [0 for _ in range(k + 1)]

        for price in prices:
            for i in range(1, len(buys)):

                buys[i] = max(buys[i], sells[i-1] - price)  # add -price to previous best after i-1 transactions
                if buys[i] == buys[i-1]:                    # additional transaction has not increased profit
                    break
                sells[i] = max(sells[i], buys[i] + price)   # add +price to max after i-1 transactions and another buy

        return max(sells)


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        return self.maxProfitWithKTransaction(prices, k)

    def maxProfitWithKTransaction(self, prices, k):
        if not prices or k <= 0:
            return 0
        evenProfits = [0 for d in prices]
        oddProfits = [0 for d in prices]
        for t in range(1, k + 1):
            maxThusFar = float('-inf')
            if t % 2 == 1:
                currentProfits = oddProfits
                previousProfits = evenProfits
            else:
                currentProfits = evenProfits
                previousProfits = oddProfits
            for d in range(1, len(prices)):
                maxThusFar = max(maxThusFar, previousProfits[d - 1] - prices[d - 1])
                currentProfits[d] = max(currentProfits[d - 1], maxThusFar + prices[d])
        return evenProfits[-1] if t % 2 == 0 else oddProfits[-1]
