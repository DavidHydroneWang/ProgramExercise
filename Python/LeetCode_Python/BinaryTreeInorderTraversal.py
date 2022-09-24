#!/usr/bin/env python
# coding=utf-8
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def preorder(root: Optional[TreeNode]) -> None:
            if not root:
                return


            preorder(root.left)
            ans.append(root.val)
            preorder(root.right)

        preorder(root)
        return ans


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:                # 二叉树为空直接返回
            return []

        res = []
        stack = []

        while root or stack:        # 根节点或栈不为空
            while root:
                stack.append(root)  # 将当前树的根节点入栈
                root = root.left    # 找到最左侧节点

            node = stack.pop()      # 遍历到最左侧，当前节点无左子树时，将最左侧节点弹出
            res.append(node.val)    # 访问该节点
            root = node.right       # 尝试访问该节点的右子树
        return res


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []

        while root or stack:
              while root:
                stack.append(root)
                root = root.left
              root = stack.pop()
              ans.append(root.val)
              root = root.right

        return ans
