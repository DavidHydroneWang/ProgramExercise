#!/usr/bin/env python
# coding=utf-8
class Solution:
    def myAtoi(self, s: str) -> int:
        my_list = s.strip()
        res = []
        sign = None

        if my_list and my_list[0] == '-':
            sign = '-'
        if my_list and (my_list[0] == '+' or my_list[0] == '-'):
            my_list = my_list[1:]
        for i in my_list:

            if i.isdigit():
                res.append(i)
            else:
                break

        result = ''.join(res)
        if sign:
            if result:
                result = sign + result

        if result:
                if int(result) < -2**31:
                    return -2**31
                elif int(result) > 2**31 - 1:
                    return 2**31 -1
                else:
                    return int(result)

        else:
            return 0


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()

        negative = False
        if str and str[0] == '-':
            negative = True
        if str and (str[0] == '+' or str[0] == '-'):
            str = str[1:]
        if not str:
            return 0

        digits = {i for i in '0123456789'}
        result = 0
        for c in str:
            if c not in digits:
                break
            result = result * 10 + int(c)

        if negative:
            result = -result

        result = max(min(result, 2**31 - 1), -2**31)
        return result


class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        max_int, min_int = 2147483647, -2147483648
        result, pos = 0, 0
        ls = len(s)
        while pos < ls and s[pos] == ' ':
            pos += 1
        if pos < ls and s[pos] == '-':
            sign = -1
            pos += 1
        elif pos < ls and s[pos] == '+':
            pos += 1
        while pos < ls and ord(s[pos]) >= ord('0') and ord(s[pos]) <= ord('9'):
            num = ord(s[pos]) - ord('0')
            if result > max_int / 10 or ( result == max_int / 10 and num >= 8):
                if sign == -1:
                    return min_int
                return max_int
            result = result * 10 + num
            pos += 1
        return  max(min( sign * result, 2**31 - 1), -2**31)
