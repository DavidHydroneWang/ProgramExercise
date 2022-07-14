#!/usr/bin/env python
# coding=utf-8


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or '' in strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        publicWordList = []
        minLength = min([len(st) for st in strs])

        for i in range(minLength):
            for word in strs:
                publicWordList.append(word[:i + 1])
            if len(set(publicWordList)) == 1:
                publicWordList = []
            else:
                return strs[0][:i]
        return strs[0][:minLength]
