#!/usr/bin/env python
# coding=utf-8
class MapSum:

    def __init__(self):

        self.data = defaultdict(int)
        self.t = defaultdict(int)


    def insert(self, key: str, val: int) -> None:
        #self.d[key] = val
        old = self.t[key]
        self.t[key] = val
        for i in range(1, len(key) + 1):
            self.data[key[:i]] += val -old



    def sum(self, prefix: str) -> int:
        return self.data[prefix]


class MapSum:

    def __init__(self):

        self.data = Trie()


    def insert(self, key: str, val: int) -> None:
        #self.d[key] = val
        self.data.insert(key, val)



    def sum(self, prefix: str) -> int:
        return self.data.search(prefix)

class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.value = 0

    def insert(self, word, value):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.isEnd = True
        cur.value = value
    def search(self, word):
        cur = self
        for ch in word:
            if ch not in cur.children:
                return 0
            cur = cur.children[ch]
        return self.dfs(cur)

    def dfs(self, root):
        if not root:
            return 0
        res = root.value
        for node in root.children.values():
            res += self.dfs(node)
        return res
