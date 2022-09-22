#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        if head.next.next is None:
            if head.val == head.next.val:
                return None
            else:
                return head
        while head.val == head.next.val:
            try:
                if head.next.val == head.next.next.val:
                    head = head.next
                else:
                    return self.deleteDuplicates(head.next.next)
            except Exception as e:
                return None
        prev = head
        curr = head.next
        nex = head.next.next

        while curr and nex:
            if curr.val == nex.val:
                try:
                    while curr.val == nex.val:
                        curr = nex
                        nex = nex.next
                    prev.next = nex
                    curr = nex
                    nex = nex.next
                except Exception as e:
                    prev.next = nex
            else:
                prev = curr
                curr = nex
                nex = nex.next

        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        if head.next.next is None:
            if head.val == head.next.val:
                return None
            else:
                return head
        #while head.val == head.next.val:
            #if head.next.val == head.next.next.val:
                #head = head.next
            #else:
                #return self.deleteDuplicates(head.next.next)

        prev = head
        curr = head.next
        nex = head.next.next

        while curr and nex:
            while prev.val == curr.val:
                try:
                    if curr.val == nex.val:
                        return self.deleteDuplicates(head.next)

                    else:
                        return self.deleteDuplicates(nex)
                except:
                    pass
            if curr.val == nex.val:
                try:
                    while curr.val == nex.val:
                        curr = nex
                        nex = nex.next
                    prev.next = nex
                    curr = nex
                    nex = nex.next
                except Exception as e:
                    prev.next = nex
            else:
                prev = curr
                curr = nex
                nex = nex.next

        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pseudo = prev = ListNode(None)
        pseudo.next = head
        node = head

        while node:

            if node.next and node.val == node.next.val:     # node begins a sequence of duplicates
                duplicate_value = node.val
                node = node.next
                while node and node.val == duplicate_value: # skip over all duplicates
                    node = node.next
                prev.next = None                            # list ends until non-duplicate found

            else:                   # node is not duplicated
                prev.next = node    # add to resulting list
                prev = node
                node = node.next

        return pseudo.next
