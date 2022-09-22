#!/usr/bin/env python
# coding=utf-8
class Solution:
    def reverseWords(self, s: str) -> str:
        my_list = s.split()
        #print(my_list)
        my_list = [ ''.join(list(i)[::-1]) for i in my_list]
        res = ' '.join(my_list)

        return res
