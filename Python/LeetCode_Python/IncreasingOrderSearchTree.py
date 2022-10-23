#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = []
        self.inOrder(root, res)
        #print(res)
        head = TreeNode(0)
        node = head
        for i in range(len(res)):
            node.right = TreeNode(res[i])
            node = node.right
        return head.right


    def inOrder(self, node, res):
        if not node:
            return

        self.inOrder(node.left, res)
        res.append(node.val)
        self.inOrder(node.right, res)
        return res


class Solution:
    def increasingBST(self, root: TreeNode, tail: TreeNode = None) -> TreeNode:
        if not root:
            return tail

        res = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        return res


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        head, tail = None, None
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if not head:
                head = cur
            else:
                tail.right = cur
            tail = cur
            cur.left = None
            cur = cur.right
        return head
