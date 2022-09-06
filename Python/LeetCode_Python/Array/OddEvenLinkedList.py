#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = []
        odd = []
        i = 1
        while head:
            if i % 2 == 0:
                even.append(head.val)
                head = head.next
                i += 1
            else:
                odd.append(head.val)
                head = head.next
                i += 1

        head = ListNode(None)
        res = head

        while odd:
            res.next = ListNode(odd.pop(0))
            res = res.next

        while even:
            res.next = ListNode(even.pop(0))
            res = res.next

        return head.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddList = ListNode(0)  # This will also serve as oddList tail node
        evenList = ListNode(0)  # This will also serve as evenList tail node
        oddListHead = oddList
        evenListHead = evenList
        isOdd = True
        while head:
            if isOdd:
                oddList.next = head
                oddList = oddList.next
            else:
                evenList.next = head
                evenList = evenList.next
            head = head.next
            isOdd = not isOdd
        evenList.next = None  # to break the cyclic list
        oddList.next = evenListHead.next
        return oddListHead.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        odd = ListNode()
        even = ListNode()
        odd_node = odd
        even_node = even
        while head:
            if not i % 2:
                odd_node.next = head
                odd_node = odd_node.next
            else:
                even_node.next = head
                even_node = even_node.next
            i += 1
            head = head.next
        odd_node.next = even.next
        even_node.next = None
        return odd.next
