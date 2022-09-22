#!/usr/bin/env python
# coding=utf-8
class Solution:
    def isPalindrome(self, x: int) -> bool:
        my_list = list(str(x))
        return my_list == my_list[::-1]A


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        left, right = 0, len(s)-1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -=1

        return True


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        copy, reverse = x, 0

        while copy:
            reverse *= 10
            reverse += copy % 10
            copy //= 10

        return x == reverse
