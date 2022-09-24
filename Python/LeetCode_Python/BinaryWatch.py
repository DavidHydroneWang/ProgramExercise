#!/usr/bin/env python
# coding=utf-8
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        hour_dict= {}
        minute_dict = {}
        for i in range(12):
            hour_dict[i] = (str(i), bin(i).count('1'))

        for i in range(10):
            minute_dict[i] = ('0' + str(i), bin(i).count('1'))

        for i in range(10, 60):
            minute_dict[i] = (str(i), bin(i).count('1'))

        #print(hour_dict)
        #print(minute_dict)
        if turnedOn > 8:
            return res
        else:
            for i in range(4):
                for key1,value1 in hour_dict.items():
                    if value1[1] == i:
                        for key2, value2 in minute_dict.items():
                            if value1[1] == turnedOn - value2[1]:
                                res.append(value1[0] + ':' + value2[0])

        return res


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        return ['%d:%02d' % (h, m)
            for h in range(12) for m in range(60)
            if (bin(h) + bin(m)).count('1') == turnedOn]
