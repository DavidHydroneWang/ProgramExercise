#!/usr/bin/env python
# coding=utf-8
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res

        q = [root]
        #q.append(root)
        #print(help(root))
        while q:
            level = []
            for _ in range(len(q)):

                node = q.pop(0)
                if node:
                    level.append(node.val)
                if node.children:
                    q.extend(node.children)
            res.append(level)
        return res


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def dfs(root, i):
            if root is None:
                return
            if len(ans) <= i:
                ans.append([])
            ans[i].append(root.val)
            for child in root.children:
                dfs(child, i + 1)

        ans = []
        dfs(root, 0)
        return ans



class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        if not root:
            return ans

        queue = [root]

        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                cur = queue.pop(0)
                level.append(cur.val)
                for child in cur.children:
                    queue.append(child)
            ans.append(level)

        return ans
