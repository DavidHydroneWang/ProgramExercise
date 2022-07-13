#!/usr/bin/env python
# coding=utf-8


class Soltution:
    def reverse(self, x: 'int') -> 'int':
        rList = []
        minus = False
        if x < 0:
            minus = True
            x = x * (-1)

        while x // 10 != 0:
            rList.append(str(x % 10))
            x = x // 10

        rList.append(x)

        length = len(rList)
        rNum = 0
        for i in range(length):
            rNum += int(rList[i]) * pow(10, length - i - 1)

        if minus:
            rNum *= -1

        if rNum in range(pow(2, 31) * (-1), pow(2, 31) - 1):
            return rNum
        else:
            0


class Soltution:
    def reverse(self, x: 'int') -> 'int':
        rList = list(str(x))
        if rList[0] == '-':
            rNum = int(''.join(rList[1:][::-1]))
        else:
            rNum = int(''.join(rList[::-1]))

        if rNum in range(pow(2, 31) * (-1), pow(2, 31) - 1):
            return rNum
        else:
            0
