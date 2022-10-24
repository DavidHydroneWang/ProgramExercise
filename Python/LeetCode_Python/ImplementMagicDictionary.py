#!/usr/bin/env python
# coding=utf-8
class MagicDictionary:

    def __init__(self):
        self.list = []


    def buildDict(self, dictionary: List[str]) -> None:
        self.list = dictionary[:]


    def search(self, searchWord: str) -> bool:
        for word in self.list:
            if word == searchWord or len(word) != len(searchWord):
                continue
            else:
                idx = 0
                for i, j in zip(word, searchWord):
                    if i != j:
                        idx += 1
                if idx == 1:
                    return True
                else:
                    continue
        return False


class MagicDictionary:

    def __init__(self):
        self.trie_tree = Trie()


    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.trie_tree.insert(word)


    def search(self, searchWord: str) -> bool:
        size = len(searchWord)
        for i in range(size):
            for j in range(26):
                new_ch = chr(ord('a') + j)
                if searchWord[i] != new_ch:
                    new_word = searchWord[:i] + new_ch + searchWord[i + 1:]
                    if self.trie_tree.search(new_word):
                        return True
        return False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.isEnd = False


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.isEnd = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]

        return cur is not None and cur.isEnd
