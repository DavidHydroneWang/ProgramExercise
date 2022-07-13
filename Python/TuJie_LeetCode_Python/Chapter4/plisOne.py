#!/usr/bin/env python
# coding=utf-8


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        flag = True
        for i in range(len(digits)):
            if flag is True:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    flag = False
        if digits[-1] == 0:
            digits.append(1)
        digits.reverse()
        return digits


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = [str(i) for i in digits]
        n = int(''.join(digits))
        n += 1
        result = [int(i) for i in list(str(n))]
        return result
