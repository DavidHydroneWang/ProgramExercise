#!/usr/bin/env python
# coding=utf-8
class Solution: # 167 / 168 test cases passed. Status: Time Limit Exceeded
    def maxProduct(self, words: List[str]) -> int:
        res = []
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not any(k in words[j] for k in words[i]):
                    res.append(len(words[i] * len(words[j])))

                else:
                    res.append(0)

        return max(res)


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        mask = [0] * n
        for i, word in enumerate(words):
            for ch in word:
                mask[i] |= 1 << (ord(ch) - ord('a'))
        ans = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if mask[i] & mask[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans



class Solution:
    def maxProduct(self, words: List[str]) -> int:
        sets, mx = {w: set(w) for w in words}, 0
        words.sort(key = len, reverse = True)
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if len(words[i]) * len(words[j]) <= mx:
                    break
                elif not sets[words[i]] & sets[words[j]]:
                    mx = len(words[i]) * len(words[j])
        return mx
