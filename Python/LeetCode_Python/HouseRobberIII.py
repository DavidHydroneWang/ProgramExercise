#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def robOrNot(root):
            if not root:
                return (0, 0)
            robLeft, notRobLeft = robOrNot(root.left)
            robRight, notRobRight = robOrNot(root.right)
            return (root.val + notRobLeft + notRobRight, max(robLeft, notRobLeft) + max(robRight, notRobRight))

        return max(robOrNot(root))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        res = self.dfs(root)
        return max(res)

    def dfs(self, root):
        if not root:
            return [0, 0]
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        val_steal = root.val + left[1] + right[1]
        val_no_steal = max(left[0], left[1]) + max(right[0], right[1])
        return [val_steal, val_no_steal]

class Solution:
    memory = {}
    def rob(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right  is None:
            return root.val
        if self.memory.get(root) is not None:
            return self.memory[root]
        # 偷父节点
        val1 = root.val
        if root.left:
            val1 += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            val1 += self.rob(root.right.left) + self.rob(root.right.right)
        # 不偷父节点
        val2 = self.rob(root.left) + self.rob(root.right)
        self.memory[root] = max(val1, val2)
        return max(val1, val2)


class Solution:

    def rob(self, root: Optional[TreeNode]) -> int:
        dp = self.traversal(root)
        return max(dp)

    def traversal(self, node):

        # 递归终止条件，就是遇到了空节点，那肯定是不偷的
        if not node:
            return (0, 0)

        left = self.traversal(node.left)
        right = self.traversal(node.right)

        # 不偷当前节点, 偷子节点
        val_0 = max(left[0], left[1]) + max(right[0], right[1])

        # 偷当前节点, 不偷子节点
        val_1 = node.val + left[0] + right[0]

        return (val_0, val_1)


class Solution:

    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return 0, 0
            l, r = dfs(node.left), dfs(node.right)
            return max(l) + max(r), node.val + l[0] + r[0]
        return max(dfs(root)
