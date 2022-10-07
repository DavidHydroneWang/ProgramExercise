#!/usr/bin/env python
# coding=utf-8
class Solution: #  36 / 71 test cases passed. Status: Time Limit Exceeded
    def findNthDigit(self, n: int) -> int:
        s = ''
        for i in range(n + 1):
            s += str(i)
        #print(s)
        return int(s[n])


class Solution:
    def findNthDigit(self, n: int) -> int:
        digits = 1
        start = 1
        base = 9
        while n > base:
            n -= base
            digits += 1
            start *= 10
            base = start * digits * 9

        number = start + (n - 1) // digits
        idx = (n - 1) % digits
        return int(str(number)[idx])


class Solution:
    def findNthDigit(self, n: int) -> int:
        count = 9
        start = 1
        curr_len = 1
        while n > curr_len * count:
            n -= curr_len * count
            curr_len += 1
            count *= 10
            start *= 10
        start += (n - 1) // curr_len
        s = str(start)
        return int(s[(n - 1) % curr_len])


class Solution:
    def findNthDigit(self, n: int) -> int:
        def get_bit_num():
            return 10 if p == 0 else 9 * pow(10, p) * (p + 1)

        if n < 10:
            return n
        p = count = 0
        while 1:
            count = get_bit_num()
            if n < count:
                break
            n -= count
            p += 1
        num = n // (p + 1) + pow(10, p)
        return int(str(num)[n % (p + 1)])
