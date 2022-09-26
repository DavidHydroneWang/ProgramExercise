#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # 37 / 52 test cases passed. Status: Time Limit Exceeded
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        if root.left:
            left = self.minDepth(root.left)
        else:
            left = None
        if root.right:
            right = self.minDepth(root.right)
        else:
            right = None
        if left and right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        elif left:
            return 1 + self.minDepth(root.left)
        elif right:
            return 1 + self.minDepth(root.right)
        else:
            return 1

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        min_depth = 10**9
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth) # 获得左子树的最小高度
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth) # 获得右子树的最小高度
        return min_depth + 1


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        que = deque()
        que.append(root)
        res = 1

        while que:
            for _ in range(len(que)):
                node = que.popleft()
                # 当左右孩子都为空的时候，说明是最低点的一层了，退出
                if not node.left and not node.right:
                    return res
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
            res += 1
        return res
