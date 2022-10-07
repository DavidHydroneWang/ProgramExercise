#!/usr/bin/env python
# coding=utf-8
class Solution: # 20 / 38 test cases passed. Status: Wrong Answer
    def countDigitOne(self, n: int) -> int:
        res = 0
        for i in range(n + 1):
            #print(i)
            res += self.Number(i)

        return res

    def Number(self, i):
        res = 0
        if i == 0:
            return res
        while i > 0:
            div, remainder = int(i/ 10), i % 10
            if div == 1:
                res += 1
            elif div == 0 and remainder ==1:
                res += 1
                break
            if div == 0 and 1 < remainder <= 9:
                break
            else:
                i = remainder
        #print(res)
        return res


class Solution:
    def countDigitOne(self, n: int) -> int:
        res = 0
        pow10 = 1

        while pow10 <= n:
            divisor = pow10 * 10
            quotient = n // divisor
            remainder = n % divisor
            if quotient > 0:
                res += quotient * pow10
            if remainder >= pow10:
                res += min(remainder - pow10 + 1, pow10)
            pow10 *= 10

        return res


class Solution:
    def countDigitOne(self, n: int) -> int:
        if n < 1:
            return 0
        s = str(n)
        high = int(s[0])
        base = pow(10, len(s) - 1)
        lows = n % base
        return (
            self.countDigitOne(base - 1) + lows + 1 + self.countDigitOne(lows)
            if high == 1
            else high * self.countDigitOne(base - 1) + base + self.countDigitOne(lows)
        )


class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        q, x, ans = n, 1, 0
        while q > 0:
            digit = q % 10
            q //= 10
            ans += q * x
            if digit == 1:
                ans += n % x + 1
            elif digit > 1:
                ans += x
            x *= 10
        return ans


class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        ones = 0

        block_size = 10
        for _ in range(len(str(n))):

            blocks, rem = divmod(n + 1, block_size)
            ones += blocks * block_size // 10       # nb blocks * nb ones in a block
            ones += min(block_size // 10, max(0, rem - block_size // 10))   # partial blocks
            block_size *= 10

        return ones
