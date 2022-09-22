#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pos = left
        stack = []
        pos = 0
        p = head
        while pos <= right - 1:
            if pos >= left - 1:
                stack.append(p.val)
            p = p.next
            pos += 1
        res = ListNode(None)
        new = res
        while stack:
            new.next = ListNode(stack.pop())
            new = new.next
        pos = 0
        result = ListNode(None)
        new2 = result
        while head is not None:
            if pos < left - 1:
                new2.next = head
                new2 = new2.next
            elif pos <= right - 1:
                new2.next = res.next
                res = res.next
                new2 = new2.next
            else:
                new2.next = head
                new2 = new2.next
            #print(result)
            head = head.next
            pos += 1
        return result.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        node = head
        stack = []
        while count != left:
            node = node.next
            count += 1
        reverse = node
        while count <= right:
            stack.append(reverse.val)
            reverse = reverse.next
            count += 1
        while stack:
            node.val = stack.pop()
            node = node.next
        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        if m == n:
            return head
        split_node, prev, curr = None, None, head
        count = 1
        while count <= m and curr is not None:
            if count == m:
                split_node = prev
            prev = curr
            curr = curr.next
            count += 1
        tail, next_node = prev, None
        while curr is not None and count <= n:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
            count += 1
        if split_node is not None:
            split_node.next = prev
        if tail is not None:
            tail.next = curr
        if m == 1:
            return prev
        return head
