#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        q = [root]

        while q:
            level = []
            for _ in range(len(q)):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(max(level))

        return res



class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def  dfs(root, depth):
            if not root:
                return
            if depth + 1 > len(res):
                res.append(root.val)
            else:
                res[depth] = max(res[depth], root.val)

            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 0)

        return res


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return root
        queue = [root]
        max_in_row = []
        while queue:
            length = len(queue)
            max_num = float(-inf)
            while length:
                length -= 1
                node = queue.pop(0)
                max_num = max(max_num, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            max_in_row.append(max_num)
        return max_in_row
