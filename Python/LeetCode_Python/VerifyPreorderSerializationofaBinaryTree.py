#!/usr/bin/env python
# coding=utf-8
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if not preorder:
            return True
        my_list = preorder.split(',')
        if len(my_list) % 2 == 0:
            return False
        expected_leaves = 1
        for node in my_list:

            if expected_leaves == 0:
                return False
            if node == '#':
                expected_leaves -= 1
            else:
                expected_leaves += 1

        return expected_leaves == 0


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if not preorder:
            return True
        my_list = preorder.split(',')
        if len(my_list) % 2 == 0:
            return False
        degree = 1
        for node in my_list:
            degree -= 1
            if degree < 0:
                return False
            if node != '#':
                degree += 2


        return degree == 0
