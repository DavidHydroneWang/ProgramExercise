#!/usr/bin/env python
# coding=utf-8
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = dict()
        for i in range(len(order)):
            order_map[order[i]] = i
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            flag = True

            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if order_map[word1[j]] > order_map[word2[j]]:
                        return False
                    else:
                        flag = False
                        break

            if flag and len(word1) > len(word2):
                return False
        return True


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict = {c: i for i, c in enumerate(order)}
        words = [[dict[c] for c in word] for word in words]
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        indices = {c: i for i, c in enumerate(order)}
        prev = []

        for word in words:
            mapping = [indices[c] for c in word]
            if mapping < prev:
                return False
            prev = mapping

        return True
