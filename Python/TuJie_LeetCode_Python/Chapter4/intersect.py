#!/usr/bin/env python
# coding=utf-8


class Solution:
    def intersect(self, num1, num2):
        """
        :type num1: List[int]
        :type num2: List[int]
        :rtype: List[int]
        """
        result = []
        num1.sort()
        num2.sort()
        p1 = 0
        p2 = 0
        while p1 < len(num1) and p2 < len(num2):
            if num1[p1] < num2[p2]:
                p1 += 1
            elif num1[p1] == num2[p2]:
                result.append(num1[p1])
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        return result


class Solution:
    def intersect(self, num1, num2):
        """
        :type num1: List[int]
        :type num2: List[int]
        :rtype: List[int]
        """
        result = []
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        for n in num1:
            if n in num2:
                result.append(n)
                num2.remove(n)
        return result
