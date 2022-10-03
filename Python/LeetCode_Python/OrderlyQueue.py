#!/usr/bin/env python
# coding=utf-8
class Solution:  # 30 / 111 test cases passed. Status: Wrong Answer
    def orderlyQueue(self, s: str, k: int) -> str:
        if not s or len(s) == 1:
            return s
        my_list = list(s)
        if k >= len(s):
            k = len(s) - 1
        flag = True
        while flag:
            for i in range(k):
                if ord(my_list[i]) > ord(my_list[-1]):
                    my_list = my_list[:i] + my_list[i + 1:] + [my_list[i]]
                    #print(my_list)
                    break
                #print(i)
                #if i >= len(s) - 1:
                    #break
                if ord(my_list[i]) > ord(my_list[i + 1]):
                    my_list = my_list[:i] + my_list[i + 1:] + [my_list[i]]
                if i == k - 1 and ord(my_list[i]) <= ord(my_list[-1]) and ord(my_list[i]) <= ord(my_list[i + 1]) :
                    flag = False

        return ''.join(my_list)


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            ans = s
            for _ in range(len(s) - 1):
                s = s[1:] + s[0]
                ans = min(ans, s)
            return ans
        return "".join(sorted(s))
