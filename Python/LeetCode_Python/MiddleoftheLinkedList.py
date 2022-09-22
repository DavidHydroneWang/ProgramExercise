#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        count = 0
        temp = head
        while temp is not None:
            count += 1
            temp = temp.next

        count = count // 2
        target = 0
        res = head
        while res is not None:
            if target == count - 1:
                res = res.next
                break
            res = res.next
            target += 1
        return res


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # def middleNode(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     res = []
    #     while head:
    #         res.append(head)
    #         head = head.next
    #     return res[len(res) / 2]

    def middleNode(self, head):
        # Fast point is 2 times faster than slow point
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
