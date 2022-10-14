#!/usr/bin/env python
# coding=utf-8
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = len(a) - 1, len(b) - 1
        arr = []
        carry = 0
        while x >= 0 or y >= 0:
            if x >= 0:
                if a[x] == '1':
                    carry += 1
                x -= 1
            if y >= 0:
                if b[y] == '1':
                    carry += 1
                y -= 1
            arr.append(chr((carry & 1) + ord('0')))
            carry >>= 1
        if carry == 1:
            arr.append('1')

        return ''.join(reversed(arr))


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a, 2)
        y = int(b, 2)
        ans = 0
        while y:
            carry = ((x & y) << 1)
            x ^= y
            y = carry
        return bin(x)[2:]
