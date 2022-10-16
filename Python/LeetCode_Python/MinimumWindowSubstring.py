#!/usr/bin/env python
# coding=utf-8
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        window = collections.defaultdict(int)
        for ch in t:
            need[ch] += 1

        left, right = 0, 0
        valid = 0
        start = 0
        size = len(s) + 1
        while right < len(s):
            insert_ch = s[right]
            right += 1
            if insert_ch in need:
                window[insert_ch] += 1
                if window[insert_ch] == need[insert_ch]:
                    valid += 1

            while valid == len(need):
                if right - left < size:
                    start = left
                    size = right - left
                remove_ch = s[left]
                left += 1
                if remove_ch in need:
                    if window[remove_ch] == need[remove_ch]:
                        valid -= 1
                    window[remove_ch] -= 1
        if size == len(s) + 1:
            return ''
        return s[start:start + size]


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        need = Counter(t)                                                                   # hash table to store char frequency
        missing = len(t)                                                                    # total number of chars we care
        left, minWindowStart, minWindowEnd = 0, 0, 0
        for right, char in enumerate(s, 1):                                                 # right pointer startes at second character of 's'
            if need[char] > 0:                                                              # char is in 't'
                missing -= 1
            need[char] -= 1
            if missing == 0:                                                                # condition to shrink window, which means it's the time to advance left. Because all target char currently is in current window
                while left < right and need[s[left]] < 0:                                   # remove chars to find the real start
                    need[s[left]] += 1
                    left += 1
                if minWindowEnd == 0 or (right - left <= minWindowEnd - minWindowStart):    #update window
                    minWindowStart, minWindowEnd = left, right
        return "" if missing > 0 else s[minWindowStart:minWindowEnd]


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if n > m:
            return ""
        need, window = defaultdict(int), defaultdict(int)
        for c in t:
            need[c] += 1
        start, minLen = 0, inf
        left, right = 0, 0
        while right < m:
            window[s[right]] += 1
            right += 1
            while self.check(need, window):
                if right - left < minLen:
                    minLen = right - left
                    start = left
                window[s[left]] -= 1
                left += 1
        return "" if minLen == inf else s[start : start + minLen]

    def check(self, need, window):
        for k, v in need.items():
            if window[k] < v:
                return False
        return True


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        required = len(t)
        bestLeft = -1
        minLength = len(s) + 1

        l = 0
        for r, c in enumerate(s):
            count[c] -= 1
            if count[c] >= 0:
                required -= 1
            while required == 0:
                if r - l + 1 < minLength:
                    bestLeft = l
                    minLength = r - l + 1
                count[s[l]] += 1
                if count[s[l]] > 0:
                      required += 1
                l += 1

        return '' if bestLeft == -1 else s[bestLeft: bestLeft + minLength]
