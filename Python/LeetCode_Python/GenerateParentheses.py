#!/usr/bin/env python
# coding=utf-8
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(parenthesis, symbol, index):
            if n * 2 == index:
                if symbol == 0:
                    parentheses.append(parenthesis)
            else:
                if symbol < n:
                    backtrack(parenthesis + '(' , symbol + 1, index + 1)
                if symbol > 0:
                    backtrack(parenthesis + ')' , symbol - 1, index + 1)

        parentheses = []
        backtrack('', 0, 0)

        return parentheses



class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(l, r, s):
            if l == 0 and r == 0:
                ans.append(s)

            if l > 0:
                dfs(l - 1, r, s + '(')
            if l < r:
                dfs(l, r - 1, s + ')')


        dfs(n, n, '')
        return ans
