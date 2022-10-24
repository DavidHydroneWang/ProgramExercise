#!/usr/bin/env python
# coding=utf-8
class Solution: # 35 / 38 test cases passed. Status: Wrong Answer
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=len,reverse=True)

        s = ''
        indices = [0]
        for i in range(len(words)):
            if words[i] not in s:

                s += words[i] + '#'
            else:
                idx = 0
                while True:
                    try:
                        start = s.index(words[i][0], idx)
                        end = s.index('#', start)

                        if (end - start) > len(words[i]):
                            idx = start + 1
                        else:
                            break
                    except Exception as e:
                        break

                if (end - start) > len(words[i]):
                    s += words[i] + '#'

        #print(s)
        return len(s)


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        string = ''
        words.sort(key=len, reverse=True)
        for word in words:
            if word + '#' not in string:
                string += word + '#'
        return len(string)



class Trie:
    def __init__(self):
        self.children = [None] * 26

    def insert(self, w):
        node = self
        pref = True
        for c in w:
            idx = ord(c) - ord("a")
            if node.children[idx] is None:
                node.children[idx] = Trie()
                pref = False
            node = node.children[idx]
        return 0 if pref else len(w) + 1


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=lambda x: -len(x))
        trie = Trie()
        return sum(trie.insert(w[::-1]) for w in words)
