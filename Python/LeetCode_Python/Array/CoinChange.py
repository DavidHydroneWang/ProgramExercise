#!/usr/bin/env python
# coding=utf-8
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        for i in range(1, amount + 1): dp[i] = min([dp[i - c] if i - c >= 0 else float('inf') for c in coins]) + 1
        return dp[amount] if dp[amount] != float('inf') else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if coins is None or len(coins) == 0:
            return -1
        coins.sort()
        dp = [ float('inf') ] * (amount + 1)
        for i in range(1, amount + 1):
            for coin in coins:
                if i == coin:
                    dp[i] = 1
                    break
                elif i > coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] ==  float('inf') :
            return -1
        return dp[amount]


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        numOfCoins = [float('inf') for n in range(amount + 1)]
        numOfCoins[0] = 0
        for coin in coins:
            for n in range(amount + 1):
                if coin <= n:
                    numOfCoins[n] = min(numOfCoins[n], numOfCoins[n - coin] + 1)
        return numOfCoins[amount] if numOfCoins[amount] != float('inf') else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        numOfCoins = [float('inf') for n in range(amount + 1)]
        numOfCoins[0] = 0
        return self.coinChangeHelper(coins, amount, numOfCoins)


    def coinChangeHelper(self, coins, remainder, numOfCoins):
        # minimum coins to make change for negative amount is -1.
        # this is just a base case we arbitrary define
        if remainder < 0:
            return -1
        # the minimum number of coins to make change for 0 is always 0
        if remainder == 0:
            return 0
        # If we already have the answer cached, just return it
        if numOfCoins[remainder] != float('inf'):
            return numOfCoins[remainder]
        # No answer yet. Try each coin as the last coin in the change that we make for the amount
        minimum = float('inf')
        for coin in coins:
            changeResultForRestAmount = self.coinChangeHelper(coins, remainder - coin, numOfCoins)
            if changeResultForRestAmount >= 0 and changeResultForRestAmount < minimum:
                minimum = changeResultForRestAmount + 1
        numOfCoins[remainder] = -1 if minimum == float('inf') else minimum
        return numOfCoins[remainder]
