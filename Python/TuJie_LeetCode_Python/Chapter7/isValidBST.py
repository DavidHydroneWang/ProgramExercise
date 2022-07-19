#!/usr/bin/env python
# coding=utf-8


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        import sys
        minval = sys.maxsize * (-1)
        maxval = sys.maxsize
        return self.validBST(root, minval, maxval)

    def validBST(self, root, minval, maxval):
        if root is None:
            return True
        if root.val <= minval or root.val >= max:
            return False
        return self.validBST(root.left, minval, root.val) and self.validBST(root.right, root.val, maxval)maxval
