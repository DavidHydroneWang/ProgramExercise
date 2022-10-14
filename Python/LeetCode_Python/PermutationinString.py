#!/usr/bin/env python
# coding=utf-8
class Solution: # 68 / 107 test cases passed. Status: Time Limit Exceeded
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from itertools import permutations as pt
        if len(s1) > len(s2):
            return False
        res = []
        s = list(s1)
        if not any(i in s2 for i in s1):
            return False
        for i in pt(s, len(s)):
            #print(i)
            temp = ''.join(i)
            if temp in s2:
                return True


        return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        window = [0 for _ in range(26)]
        for i in range(n1):
            window[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] -= 1
        if self.check(window):
            return True
        for i in range(n1, n2):
            window[ord(s2[i]) - ord('a')] -= 1
            window[ord(s2[i - n1]) - ord('a')] += 1
            if self.check(window):
                return True
        return False

    def check(self, window: List[int]) -> bool:
        return all([cnt == 0 for cnt in window])


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, 0
        s1_counter = collections.Counter(s1)
        window_count = collections.Counter()
        window_size = len(s1)

        while right < len(s2):
            window_count[s2[right]] += 1

            if right - left + 1 >= window_size:
                if window_count == s1_counter:
                    return True
                window_count[s2[left]] -= 1
                if window_count[s2[left]] == 0:
                    del window_count[s2[left]]

                left += 1
            right += 1
        return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        freq = [0] * 26     # counts of each char

        for c in s1:
            freq[ord(c) - ord("a")] += 1

        for i, c in enumerate(s2):

            freq[ord(c) - ord("a")] -= 1    # decrement count of letter added to window
            if i >= n1:
                freq[ord(s2[i - n1]) - ord("a")] += 1   # increment count of letter exiting window

            if not any(freq):
                return True

        return False
