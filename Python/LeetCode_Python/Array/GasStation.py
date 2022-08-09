#!/usr/bin/env python
# coding=utf-8
# time limit exceeded
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            currentGas = 0
            j = i
            while True:
                currentGas += gas[j]
                if currentGas < cost[j]:
                    break
                else:
                    currentGas -= cost[j]
                    j =  ( j + 1) % len(gas)
                    if j == i:
                        if currentGas + gas[j] >= cost[j]:
                            return i
                        else:
                            break
        return -1


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        currentGas = 0
        res = None
        for i in range(len(gas)):
            currentGas += gas[i]
            if currentGas < cost[i]:
                currentGas = 0
                res = None
            else:
                currentGas -= cost[i]
                if res is None:
                    res = i

        return res
