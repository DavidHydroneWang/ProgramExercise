#!/usr/bin/env python
# coding=utf-8
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, presum):
            if root is None:
                return 0
            s = 10 * presum + root.val
            if root.left is None and root.right is None:
                return s
            return dfs(root.left, s) + dfs(root.right, s)

        return dfs(root, 0)


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(root: Optional[TreeNode], path: int) -> None:
            nonlocal ans
            if not root:
                return
            if not root.left and not root.right:
                ans += path * 10 + root.val
                return

            dfs(root.left, path * 10 + root.val)
            dfs(root.right, path * 10 + root.val)

        dfs(root, 0)
        return ans


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        path = []
        def backtrace(root):
            nonlocal res
            if not root: return # 节点空则返回
            path.append(root.val)
            if not root.left and not root.right: # 遇到了叶子节点
                res += get_sum(path)
            if root.left: # 左子树不空
                backtrace(root.left)
            if root.right: # 右子树不空
                backtrace(root.right)
            path.pop()

        def get_sum(arr):
            s = 0
            for i in range(len(arr)):
                s = s * 10 + arr[i]
            return s

        backtrace(root)
        return res
