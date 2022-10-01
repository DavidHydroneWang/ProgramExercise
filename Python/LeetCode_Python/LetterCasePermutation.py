#!/usr/bin/env python
# coding=utf-8
class Solution:

    def dfs(self, s, path, i, ans):
        if i == len(s):
            ans.append(path)
            return

        self.dfs(s, path + s[i], i + 1, ans)
        if ord('a') <= ord(s[i]) <= ord('z'):
            self.dfs(s, path + s[i].upper(), i + 1, ans)
        elif ord('A') <= ord(s[i]) <= ord('Z'):
            self.dfs(s, path + s[i].lower(), i + 1, ans)

    def letterCasePermutation(self, s: str) -> List[str]:
        ans, path = [], ""
        self.dfs(s, path, 0, ans)
        return ans


class Solution:

    def letterCasePermutation(self, S: str) -> List[str]:
        bfs = ['']
        for c in S:
            if c.isdigit():
                bfs = [s + c for s in bfs]
            else:
                bfs = [s + c.lower() for s in bfs] + [s + c.upper() for s in bfs]
        return bfs
