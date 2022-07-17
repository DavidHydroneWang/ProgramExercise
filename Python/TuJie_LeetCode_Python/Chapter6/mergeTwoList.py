#!/usr/bin/env python
# coding=utf-8


def mergeTwoList(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 is None and l2 is None:
        return None
    fakeNode = ListNode(0)
    head = fakeNode
    while l1 is not None or l2 is not None:
        if l1 is None:
            head.next = l2
            l2 = l2.next
            head = head.next
        elif l2 is None:
            head.next = l1
            l1 = l1.next
            head = head.next
        else:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
                head = head.next
            else:
                head.next = l2
                l2 = l2.next
                head = head.next
    return fakeNode.next
