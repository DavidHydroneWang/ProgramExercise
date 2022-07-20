#!/usr/bin/env python
# coding=utf-8


class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rList = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                rList.append('FizzBuzz')
            elif i % 3 == 0:
                rList.append('Fizz')
            elif i % 5 == 0:
                rList.append('Buzz')
            else:
                rList.append(str(i))
        return rList
