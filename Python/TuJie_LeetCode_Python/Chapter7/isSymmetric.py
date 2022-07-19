#!/usr/bin/env python
# coding=utf-8


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.symmetricTree(root.left, root.right)

    def symmetricTree(self, left, right):
        if not left and not right:
            return True
        elif left and right and left.val == right.val:
            return self.symmetricTree(left.left, left.right) and self.symmetricTree(right.left, right.right)
        else:
            return False
