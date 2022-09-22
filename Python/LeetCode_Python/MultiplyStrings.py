#!/usr/bin/env python
# coding=utf-8
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        res = ''
        ls1, ls2, = len(num1), len(num2)
        ls = ls1 + ls2
        # list stores int
        arr = [0] * ls
        for i in reversed(range(ls1)):
            for j in reversed(range(ls2)):
                # store the direct results of multiply two ints
                arr[i + j + 1] += int(num1[i]) * int(num2[j])
        for i in reversed(range(1, ls)):
            # digital plus
            arr[i - 1] += arr[i] // 10
            arr[i] %= 10
        pos = 0
        # to string
        if arr[pos] == 0:
            pos += 1
        while pos < ls:
            res = res + str(arr[pos])
            pos += 1
        return res


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dic, l1, l2 = {str(i): i for i in range(10)}, len(num1) - 1, len(num2) - 1
        return str(sum([dic[n1] * (10**(l1-i)) for i, n1 in enumerate(num1)]) * sum([dic[n2] * (10**(l2-j)) for j, n2 in enumerate(num2)]))


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        len1, len2 = len(num1), len(num2)
        nums = [0 for _ in range(len1 + len2)]

        for i in range(len1 - 1, -1, -1):
            digit1 = int(num1[i])
            for j in range(len2 - 1, -1, -1):
                digit2 = int(num2[j])
                nums[i + j + 1] += digit1 * digit2

        for i in range(len1 + len2 - 1, 0, -1):
            nums[i - 1] += nums[i] // 10
            nums[i] %= 10

        if nums[0] == 0:
            ans = "".join(str(digit) for digit in nums[1:])
        else:
            ans = "".join(str(digit) for digit in nums[:])
        return ans
