#!/usr/bin/env python
# coding=utf-8
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = (1 << 31) - 1
        INT_MIN = - (1 << 31)
        sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
        a = abs(dividend)
        b = abs(divisor)
        tot = 0
        while a >= b:
            cnt = 0
            while a >= (b << (cnt + 1)):
                cnt += 1

            tot += 1 << cnt
            a -= b << cnt
        return sign * tot if INT_MIN <= sign * tot <= INT_MAX else INT_MAX



class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
        ans = 0
        dvd = abs(dividend)
        dvs = abs(divisor)

        while dvd >= dvs:
            k = 1
            while k * 2 * dvs <= dvd:
                k <<= 1
            dvd -= k * dvs
            ans += k

        return sign * ans


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN_INT, MAX_INT = -2147483648, 2147483647
        # 标记被除数和除数是否异号
        symbol = True if (dividend ^ divisor) < 0 else False
        # 将被除数和除数转换为正数处理
        if dividend < 0:
            dividend = -dividend
        if divisor < 0:
            divisor = -divisor

        # 除数不断左移，移位到位数大于或等于被除数
        count = 0
        while dividend >= divisor:
            count += 1
            divisor <<= 1

        # 向右移位，不断模拟二进制除法运算
        res = 0
        while count > 0:
            count -= 1
            divisor >>= 1
            if dividend >= divisor:
                res += (1 << count)
                dividend -= divisor
        if symbol:
            res = -res
        if MIN_INT <= res <= MAX_INT:
            return res
        else:
            return MAX_INT
