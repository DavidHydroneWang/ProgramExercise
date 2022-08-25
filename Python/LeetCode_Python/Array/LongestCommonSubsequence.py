#!/usr/bin/env python
# coding=utf-8
class Solution: wrong answer
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res = []
        for i in range(len(text1)):
            flag = i
            temp = text1[i]
            #print(temp)
            try:
                index = text2.index(temp)
                #print(index)
                if index == len(text2) - 1:
                    res.append(temp)
                    break
                for j in range(index + 1, len(text2)):
                    if text2[j] in text1[flag + 1:]:
                        temp += text2[j]
                        flag = text1.index(text2[j], flag + 1)
                        res.append(temp)
                        #print(temp, flag)
                    res.append(temp)

            except Exception as e:
                pass
        #print(res)
        result = [len(i) for i in res]
        if result:
            return max(result)
        return 0


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        lcs = [0 for _ in range(n + 1)]

        for c1 in text1:            # for prefix of text1 up to and including c1
            new_lcs = [0]
            for j, c2 in enumerate(text2):  # for prefix of text2 up to and including c2
                if c1 == c2:
                    new_lcs.append(1 + lcs[j])
                else:
                    new_lcs.append(max(new_lcs[-1], lcs[j + 1]))
            lcs = new_lcs

        return lcs[-1]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j - 1] + 1 if text1[i - 1] == text2[j - 1] else max(dp[i][j - 1], dp[i - 1][j])
        return dp[-1][-1]
