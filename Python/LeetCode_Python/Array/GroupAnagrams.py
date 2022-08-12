#!/usr/bin/env python
# coding=utf-8
class Solution: # Time Limit exceeded
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        back = []
        for i in range(len(strs)):
            strset = sorted(strs[i])
            if strset not in back:
                back.append(strset)
                temp = [strs[i]]
                for j in range(i + 1, len(strs)):
                    if sorted(strs[j]) == back[-1]:
                        temp.append(strs[j])

                res.append(temp)

        return res


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for i in strs:
            key = ''.join(sorted(i))

            try:
                res[key].append(i)
            except:
                res[key] = [i]
        return res.values()


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_words = defaultdict(list)

        for word in strs:
            letter_list = [c for c in word]
            letter_list.sort()
            sorted_word = "".join(letter_list)
            sorted_words[sorted_word].append(word)

        return list(sorted_words.values())
