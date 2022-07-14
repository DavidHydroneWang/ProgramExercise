#!/usr/bin/env python
# coding=utf-8


class Solution:
    def countAndSay(self, n: int) -> str:
        if n not in range(1, 31):
            return 'the number is error, quit...'
        if n == 1:
            return '1'
        rawStr = '1'
        countList = []
        pointer = 0
        while n > 1:
            if pointer + 1 < len(rawStr):
                if rawStr[pointer] == rawStr[pointer + 1]:
                    pointer += 1
                else:
                    countList.append(str(pointer + 1))
                    countList.append(rawStr(pointer))
                    rawStr = rawStr[pointer + 1:]
                    pointer = 0
                continue
            else:
                countList.append(str(pointer + 1))
                countList.append(rawStr[pointer])
                rawStr = ''.join(countList)
                countList = []
                pointer = 0
            n -= 1
        return rawStr
