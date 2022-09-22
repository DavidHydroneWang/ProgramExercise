#!/usr/bin/env python
# coding=utf-8
class Solution:
    def reverseKGroup(self , head: ListNode, k: int) -> ListNode:
        # write code here
        lastNodeOfFirstReversedPart = None
        dummyNode = ListNode(0)
        dummyNode.next = lastNodeOfFirstReversedPart
        linkedListLength = self.getLength(head)
        while True:
            newHeadOfUnreversedPart, headOfReversedPart = None, None
            if self.canReverse(linkedListLength, k):
                newHeadOfUnreversedPart, headOfReversedPart = self.reverseList(head, k)
                linkedListLength -= k
                if lastNodeOfFirstReversedPart:
                    lastNodeOfFirstReversedPart.next = headOfReversedPart
                else:
                    dummyNode.next = headOfReversedPart
                lastNodeOfFirstReversedPart = head
                head = newHeadOfUnreversedPart
            else:
                if lastNodeOfFirstReversedPart:
                    lastNodeOfFirstReversedPart.next = head
                else:
                    dummyNode.next = head
                break
        return dummyNode.next


    def canReverse(self, length, k):
        return True if length // k >= 1 else False


    def getLength(self, head):
        count, currentNode = 0, head
        while currentNode:
            currentNode = currentNode.next
            count += 1
        return count


    def reverseList(self, head, k):
        previousNode, currentNode, nextNode = None, head, head
        while k > 0 and currentNode:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode
            k -= 1
        return (currentNode, previousNode)


class Solution:
    def reverseKGroup(self , head: ListNode, k: int) -> ListNode:
        # write code here
        def reverse(h, k):
            t = h
            for i in range(k):
                if not t:
                    return h, None
                t = t.next
            pre, cur, next = None, h, h.next
            for i in range(k):

                cur.next = pre
                pre, cur, next = cur, next, next.next if next else None
            return pre, cur
        # write code here

        pre_tail = None
        cur = head
        head = None
        while cur:
            new_head, next_node = reverse(cur, k)
            if head is None:
                head = new_head
            if pre_tail:
                pre_tail.next = new_head
            pre_tail = cur
            cur = next_node
        return head
