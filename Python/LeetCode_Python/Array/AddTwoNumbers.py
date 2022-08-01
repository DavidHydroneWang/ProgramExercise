#!/usr/bin/env python
# coding=utf-8


class LinkedList:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, num1, num2):
        """
        :type num1: LinkedList
        :type num2: LinkedList
        :rtype: LinkedList
        """
        get_value = self.getRest(num1, num2)
        root = LinkedList(get_value[0])
        rest_value = get_value[1]
        num1 = num1.next
        num2 = num2.next

        backup_root = root

        while num1 is not None or num2 is not None:
            get_value = self.getRest(num1, num2, rest_value)
            new_node = LinkedList(get_value[0])
            rest_value = get_value[1]

            root.next = new_node
            root = new_node

            num1 = num1.next if num1 else None
            num2 = num2.next if num2 else None
        if rest_value:
            root.next = LinkedList(rest_value)
        return backup_root

    def getRest(self, num1, num2, rest=0):
        num1_val = num1.val if num1 else 0
        num2_val = num2.val if num2 else 0

        return ((num1_val + num2_val + rest) % 10,
                (num1_val + num2_val + rest) // 10)
