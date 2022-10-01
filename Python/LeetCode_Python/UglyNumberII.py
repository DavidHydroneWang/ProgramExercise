#!/usr/bin/env python
# coding=utf-8
class Solution: # 490 / 596 test cases passed. Status: Time Limit Exceeded
    def nthUglyNumber(self, n: int) -> int:
        res = [1, 2, 3, 4, 5]
        if n <= 5:
            return res[n - 1]
        for i in range(6, n + 1):
            minV = float('inf')
            for j in res[1:]:
                if j * 5 <= res[-1]:
                    continue
                else:
                    fac5 = j * 5
                if j * 3 <= res[-1]:
                    fac3 = float('inf')
                else:
                    fac3 = j *3
                if j * 2 <= res[-1]:
                    fac2 = float('inf')
                else:
                    fac2 = j * 2

                minV = min(minV, fac2, fac3, fac5)

            res.append(minV)
        #print(res)
        return res[n - 1]


class Solution:
    def nthUglyNumber(self, n: int) -> int:

        nums = [1]
        i2 = 0
        i3 = 0
        i5 = 0

        while len(nums) < n:
            next2 = nums[i2] * 2
            next3 = nums[i3] * 3
            next5 = nums[i5] * 5
            next = min(next2, next3, next5)
            if next == next2:
                i2 += 1
            if next == next3:
                i3 += 1
            if next == next5:
                i5 += 1
            nums.append(next)

        return nums[-1]


class Solution:
    def nthUglyNumber(self, n: int) -> int:

        dp = [1 for _ in range(n)]
        p2, p3, p5 = 0, 0, 0
        for i in range(1, n):
            dp[i] = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
            if dp[i] == dp[p2] * 2:
                p2 += 1
            if dp[i] == dp[p3] * 3:
                p3 += 1
            if dp[i] == dp[p5] * 5:
                p5 += 1
        return dp[n - 1]
