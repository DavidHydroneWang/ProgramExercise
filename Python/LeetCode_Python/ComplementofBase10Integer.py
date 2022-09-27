#!/usr/bin/env python
# coding=utf-8
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        s = bin(n)
        res = []
        for i in s[2:]:
            if i == '1':
                res.append('0')
            else:
                res.append('1')

        return int(''.join(res), 2)


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:          # special case because 0 has bit_length of 1
            return 1
        return (2**n.bit_length() - 1) - n
