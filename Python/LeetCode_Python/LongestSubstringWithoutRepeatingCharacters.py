#!/usr/bin/env python
# coding=utf-8
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        res = []
        i = 0
        while i < len(s):
            temp = []
            j = i
            while True and j < len(s):
                #print(i)
                if s[j] not in temp:
                    temp.append(s[j])
                    j += 1
                    if j == len(s) - 1:
                        res.append(temp)
                else:
                    res.append(temp)
                    break
            i += 1
        #print(res)
        ans = [ len(i) for i in res]
        return max(ans)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = res = 0

        chars = set()
        while i < len(s):
            while s[i] in chars:
                if s[j] in chars:
                    chars.remove(s[j])
                j += 1
            chars.add(s[i])
            res = max(res, i - j + 1)
            i += 1
        return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 1
        lss = 0
        length = len(s)
        if length < 2:
            return length
        s += s[-1]
        while j <= length:
            if len(set(s[i:j])) < len(s[i:j]):
                i += 1
            lss = max(lss, len(s[i:j]))
            j += 1
        return lss


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}      # mapping from character to its last seen index in s
        start = 0           # start index of current substring
        longest = 0

        for i, c in enumerate(s):

            if c in last_seen and last_seen[c] >= start:
                # start a new substring after the previous sighting of c
                start = last_seen[c] + 1
            else:
                longest = max(longest, i - start + 1)

            last_seen[c] = i    # update the last sighting index

        return longest



    class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        window = dict()
        ans = 0

        while right < len(s):
            if s[right] not in window:
                window[s[right]] = 1
            else:
                window[s[right]] += 1

            while window[s[right]] > 1:
                window[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)
            right += 1

        return ans
