#!/usr/bin/env python
# coding=utf-8


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations as cb
        res, dic = [], set()
        for i in range(len(nums) + 1):
            for item in cb(nums, i):
                item = tuple(sorted(item))
                if item not in dic:
                    dic.add(item)
                    res.append(item)
        return res


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(s: int, path: List[int]) -> None:
            ans.append(path)
            if s == len(nums):
                return

            for i in range(s, len(nums)):
                if i > s and nums[i] == nums[i - 1]:
                    continue
                dfs(i + 1, path + [nums[i]])

        nums.sort()
        dfs(0, [])
        return ans

class Solution:
    def backtrack(self, nums, index, res, path):
        res.append(path[:])

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.backtrack(nums, i + 1, res, path)
            path.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, path = [], []
        self.backtrack(nums, 0, res, path)
        return res


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)                       # n 为集合 nums 的元素个数
        sub_sets = []                       # sub_sets 用于保存所有子集
        for i in range(1 << n):             # 枚举 0 ~ 2^n - 1
            sub_set = []                    # sub_set 用于保存当前子集
            flag = True                     # flag 用于判断重复元素
            for j in range(n):  # 枚举第 i 位元素
                if i >> j & 1:  # 如果第 i 为元素对应二进制位为 1，则表示选取该元素
                    if j > 0 and (i >> (j - 1) & 1) == 0 and nums[j] == nums[j - 1]:
                        flag = False        # 如果出现重复元素，则跳过当前生成的子集
                        break
                    sub_set.append(nums[j]) # 将选取的元素加入到子集 sub_set 中
            if flag:
                sub_sets.append(sub_set)    # 将子集 sub_set 加入到所有子集数组 sub_sets 中
        return sub_sets                     # 返回所有子集


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        begin = 0
        for index in range(len(nums)):
            if index == 0 or nums[index] != nums[index - 1]:
                # generate all
                begin = 0
            size = len(res)
            # use existing subsets to generate new subsets
            for j in range(begin, size):
                curr = list(res[j])
                curr.append(nums[index])
                res.append(curr)
            # avoid duplicate subsets
            begin = size
        return res
