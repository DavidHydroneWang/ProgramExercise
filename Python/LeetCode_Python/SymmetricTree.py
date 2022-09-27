#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # 195 / 198 test cases passed. Status: Wrong Answer
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        res = []
        self.inOrder(root, res)
        print(res)
        n = len(res)
        start, end = 0, n - 1
        while start < end:
            if res[start] != res[end]:
                return False
            start += 1
            end -= 1
        return True


    def inOrder(self, root, res):
        if not root:
            return
        self.inOrder(root.left, res)
        res.append(root.val)
        self.inOrder(root.right, res)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        res = []
        self.inOrder(root, res)
        #print(res)
        n = len(res)
        start, end = 0, n - 1
        while start < end:
            if res[start][0] != res[end][0] or res[start][1] == res[end][1]:
                return False
            start += 1
            end -= 1
        return True


    def inOrder(self, root, res, flag=None):
        if not root:
            return
        self.inOrder(root.left, res, flag='left')
        res.append((root.val, flag))
        self.inOrder(root.right, res, flag='right')


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSymmetric(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p or not q:
                return p == q

            return p.val == q.val and \
                isSymmetric(p.left, q.right) and \
                isSymmetric(p.right, q.left)

        return isSymmetric(root, root)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
           if root == None:
            return True
        return self.check(root.left, root.right)

    def check(self, left: TreeNode, right: TreeNode):
        if left == None and right == None:
            return True
        elif left == None and right != None:
            return False
        elif left != None and right == None:
            return False
        elif left.val != right.val:
            return False

        return self.check(left.left, right.right) and self.check(left.right, right.left)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        while queue:
            length = len(queue)
            level = []
            while length:
                node = queue.pop(0)
                level.append(node.val if node else None)
                length -= 1
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
            i = 0
            j = len(level) - 1
            while i <= j:
                if level[i] != level[j]:
                    return False
                i += 1
                j -= 1
        return True
