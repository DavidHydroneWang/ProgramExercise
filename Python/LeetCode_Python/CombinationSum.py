#!/usr/bin/env python
# coding=utf-8
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def dfs(s, u, t):
            if s == target:
                res.append(t.copy())
                return
            if s > target:
                return
            for i in range(u, n):
                c = candidates[i]
                t.append(c)
                dfs(s + c, i, t)
                t.pop()
        dfs(0, 0, [])
        return res


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(s: int, target: int, path: List[int]) -> None:
            if target < 0:
                return
            if target == 0:
                ans.append(path.copy())
                return

            for i in range(s, len(candidates)):
                path.append(candidates[i])
                dfs(i, target - candidates[i], path)
                path.pop()

        candidates.sort()
        dfs(0, target, [])
        return ans


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        dp = [[] for _ in range(target + 1)]
        dp[0].append([])
        for i in range(1, target + 1):
            for j in range(len(candidates)):
                if candidates[j] > i:
                    break
                for k in range(len(dp[i - candidates[j]])):
                    temp = dp[i - candidates[j]][k][:]
                    if len(temp) > 0 and temp[-1] > candidates[j]:
                        continue
                    temp.append(candidates[j])
                    dp[i].append(temp)
        return dp[target]
