#!/usr/bin/env python
# coding=utf-8
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        if n > m:
            return []
        window, ans = [0 for _ in range(26)], []
        for i in range(n):
            window[ord(p[i]) - ord('a')] += 1
            window[ord(s[i]) - ord('a')] -= 1
        if self.check(window):
            ans.append(0)
        for i in range(n, m):
            window[ord(s[i]) - ord('a')] -= 1
            window[ord(s[i - n]) - ord('a')] += 1
            if self.check(window):
                ans.append(i - n + 1)
        return ans

    def check(self, window: List[int]) -> bool:
        return all([cnt == 0 for cnt in window])


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        need = collections.defaultdict(int)
        for ch in p:
            need[ch] += 1

        window = collections.defaultdict(int)
        window_size = len(p)
        res = []
        left, right = 0, 0
        valid = 0
        while right < len(s):
            if s[right] in need:
                window[s[right]] += 1
                if window[s[right]] == need[s[right]]:
                    valid += 1

            if right - left + 1 >= window_size:
                if valid == len(need):
                    res.append(left)
                if s[left] in need:
                    if window[s[left]] == need[s[left]]:
                        valid -= 1
                    window[s[left]] -= 1
                left += 1
            right += 1
        return res
