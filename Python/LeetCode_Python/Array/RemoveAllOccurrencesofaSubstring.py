#!/usr/bin/env python
# coding=utf-8
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        length = len(part)
        for i in s:
            #print(not stack)
            if not stack or  not (''.join(stack[-length:]) == part):
                stack.append(i)
            else:
                for j in range(length):
                    stack.pop()
                stack.append(i)
            #print(stack)
        if (''.join(stack[-length:]) == part):
            for j in range(length):
                stack.pop()

        return ''.join(stack)


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        def getPrefix(pattern):
            prefix = [-1]*len(pattern)
            j = -1
            for i in range(1, len(pattern)):
                while j != -1 and pattern[j+1] != pattern[i]:
                    j = prefix[j]
                if pattern[j+1] == pattern[i]:
                    j += 1
                prefix[i] = j
            return prefix

        prefix = getPrefix(part)
        result, lookup = [], []
        i = -1
        for c in s:
            while i != -1 and part[i+1] != c:
                i = prefix[i]
            if part[i+1] == c:
                i += 1
            result.append(c)
            lookup.append(i)
            if i == len(part)-1:
                result[len(result)-len(part):] = []
                lookup[len(lookup)-len(part):] = []
                i = lookup[-1] if lookup else -1
        return "".join(result)
