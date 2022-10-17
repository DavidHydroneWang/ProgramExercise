#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.

        """
        stack = []
        temp = head
        while temp:
            stack.append(temp.val)
            temp = temp.next

        length = len(stack)
        if length % 2 == 0:
            even = stack[1:length// 2 ]
            odd = stack[length// 2:]
        else:
            even = stack[1:length// 2 + 1]
            odd = stack[length// 2:]
        odd.reverse()
        #print(even, odd)
        #print(head)
        res = head
        for i in range(0, length):

            if i == 0:
                continue
            if i % 2 == 0:
                res.next = ListNode(even.pop(0))
            elif i % 2 == 1:
                res.next = ListNode(odd.pop(0))
            res = res.next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.

        """
        if not head:
            return

        vec = []
        node = head
        while node:
            vec.append(node)
            node = node.next

        left, right = 0, len(vec) - 1
        while left < right:
            vec[left].next = vec[right]
            left += 1
            if left == right:
                break
            vec[right].next = vec[left]
            right -= 1
        vec[left].next = None


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.

        """
        d = collections.deque()
        tmp = head
        while tmp.next: # 链表除了首元素全部加入双向队列
            d.append(tmp.next)
            tmp = tmp.next
        tmp = head
        while len(d): # 一后一前加入链表
            tmp.next = d.pop()
            tmp = tmp.next
            if len(d):
                tmp.next = d.popleft()
                tmp = tmp.next
        tmp.next = None # 尾部置空


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.

        """
        stack = []
        node = head
        while node:
            stack.append(node.val)
            node = node.next
        while stack:
            head.val = stack.pop(0)
            head = head.next
            if stack:
                head.val = stack.pop()
                head = head.next
