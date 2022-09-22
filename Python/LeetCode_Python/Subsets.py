#!/usr/bin/env python
# coding=utf-8
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations as cb
        if not nums:
            return [nums]
        res = []
        for i in range(len(nums) + 1):
            for j in cb(nums, i):

                res.append(list(j))
        #print(res)
        return res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(s: int, path: List[int]) -> None:
            ans.append(path)

            for i in range(s, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return ans


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []  # 存放所有符合条件结果的集合
        path = []  # 存放当前符合条件的结果
        def backtracking(nums, index):          # 正在考虑可选元素列表中第 index 个元素
            res.append(path[:])                 # 将当前符合条件的结果放入集合中
            if index >= len(nums):              # 遇到终止条件（本题）
                return

            for i in range(index, len(nums)):   # 枚举可选元素列表
                path.append(nums[i])            # 选择元素
                backtracking(nums, i + 1)       # 递归搜索
                path.pop()                      # 撤销选择

        backtracking(nums, 0)
        return res

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)                       # n 为集合 nums 的元素个数
        sub_sets = []                       # sub_sets 用于保存所有子集
        for i in range(1 << n):             # 枚举 0 ~ 2^n - 1
            sub_set = []                    # sub_set 用于保存当前子集
            for j in range(n):              # 枚举第 i 位元素
                if i >> j & 1:              # 如果第 i 为元素对应二进制位为 1，则表示选取该元素
                    sub_set.append(nums[j]) # 将选取的元素加入到子集 sub_set 中
            sub_sets.append(sub_set)        # 将子集 sub_set 加入到所有子集数组 sub_sets 中
        return sub_sets                     # 返回所有子集


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [item+[num] for item in res]
        return res                   # 返回所有子集
