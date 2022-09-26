#!/usr/bin/env python
# coding=utf-8
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return []

        q = deque([root])

        while q:
            currLevel = []
            for _ in range(len(q)):
                node = q.popleft()
                currLevel.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(currLevel)

        res.reverse()
        return res


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversal = []
        self.inorder(root, 0, traversal)
        return traversal[::-1]

    def inorder(self, node, depth, traversal):

        if not node:
            return

        if len(traversal) == depth:
            traversal.append([])

        self.inorder(node.left, depth+1, traversal)

        traversal[depth].append(node.val)

        self.inorder(node.right, depth+1, traversal)
