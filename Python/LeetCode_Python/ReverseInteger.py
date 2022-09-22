#!/usr/bin/env python
# coding=utf-8
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            carry = '-'
            my_list = list(str(x)[1:])
        else:
            carry = '+'
            my_list = list(str(x))

        my_list.reverse()

        string =  carry + ''.join(my_list)

        if int(string) < -2**31 or int(string) > 2**31 - 1:
            return 0
        return int(string)
