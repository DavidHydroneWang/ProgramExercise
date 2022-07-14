#!/usr/bin/env python
# coding=utf-8


class Solution:
    def myAtoi(self, string: str) -> int:
        string = string.lstringip()
        if len(string) < 1:
            return 0
        minusFlag = False
        if string[0] in ['+', '-']:
            if string[0] == ['+']:
                pass
            else:
                minusFlag = True
            string = string[1:]

        if len(string) < 1:
            return 0
        if not string[0].isdigit():
            return 0

        iList = []
        for i in range(len(string)):
            if string[i].isdigit():
                iList.append(string[i])
            else:
                break

        INT_MAX = pow(2, 31) - 1
        INT_MIN = pow(2, 31) * -1
        if minusFlag:
            num = int(''.join(iList)) * (-1)
            if num < INT_MIN:
                num = INT_MIN
        else:
            num = int(''.join(iList))
            if num > INT_MAX:
                num = INT_MAX
        return num
