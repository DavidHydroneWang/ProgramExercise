#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.res = [-1]
        def inOrder(node, res):
            if not node:
                return

            inOrder(node.left, res)
            res.append(node.val)
            inOrder(node.right, res)
        inOrder(root, self.res)


    def next(self) -> int:
        if self.hasNext:
            self.res.pop(0)
            return self.res[0]

        else:
            return -1


    def hasNext(self) -> bool:
        try:
            self.res[1]
            return True
        except Exception as e:
            return False


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        def inorder(root):
            if root:
                inorder(root.left)
                self.vals.append(root.val)
                inorder(root.right)

        self.cur = 0
        self.vals = []
        inorder(root)

    def next(self) -> int:
        res = self.vals[self.cur]
        self.cur += 1
        return res

    def hasNext(self) -> bool:
        return self.cur < len(self.vals)

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        cur = self.stack.pop()
        node = cur.right
        while node:
            self.stack.append(node)
            node = node.left
        return cur.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
