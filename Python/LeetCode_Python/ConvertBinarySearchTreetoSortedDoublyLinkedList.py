#!/usr/bin/env python
# coding=utf-8
class Solution:
    def Convert(self , pRootOfTree ):
        # write code here
        if not pRootOfTree:
            return

        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        res = []
        self.inOrder(pRootOfTree, res)
        #print(res)
        for i in range(len(res) - 2, -1, -1):
            if i == 0:
                prev = curr
                curr = TreeNode(res[i])
                curr.right = prev
                prev.left = curr
            elif i == len(res) - 2:
                curr = TreeNode(res[i])
                prev = TreeNode(res[i + 1])
                curr.right = prev
                prev.left = curr
            else:
                prev = curr
                curr = TreeNode(res[i])
                curr.right = prev
                prev.left = curr
        return curr

    def inOrder(self, root, res):
        if not root:
            return
        self.inOrder(root.left, res)
        res.append(root.val)
        self.inOrder(root.right, res)


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(node: 'Node'):
            if not node:
                return

            dfs(node.left)
            if self.tail:
                self.tail.right = node
                node.left = self.tail
            else:
                self.head = node
            self.tail = node
            dfs(node.right)

        if not root:
            return None

        self.head, self.tail = None, None
        dfs(root)
        self.head.left = self.tail
        self.tail.right = self.head
        return self.head

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        left_head = self.treeToDoublyList(root.left)
        right_head = self.treeToDoublyList(root.right)

        if left_head:
            root.left = left_head.left      # link root to tail of left subtree
            left_head.left.right = root
        else:
            left_head = root                # no subtree on left, root is left_head

        if right_head:
            root.right = right_head         # link root to head of right_subtree
            right_tail = right_head.left    # store right_tail
            right_head.left = root
        else:
            right_tail = root               # no subtree on right, root is right_tail

        left_head.left = right_tail         # link head and tail
        right_tail.right = left_head

        return left_head
