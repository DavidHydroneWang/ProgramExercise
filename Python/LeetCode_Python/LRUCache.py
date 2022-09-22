#!/usr/bin/env python
# coding=utf-8
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.queue = []

    def update(self, key):
        self.queue.remove(key)
        self.queue.insert(0, key)

    def get(self, key: int) -> int:
        if key in self.cache:
            self.update(key)
            return self.cache[key]
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.queue.remove(key)
        elif len(self.queue) == self.capacity:
            del self.cache[self.queue.pop(-1)]

        self.cache[key] = value
        self.queue.insert(0, key)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class LRUCache:

    def remove(self, node):
        node.pre.next, node.next.pre = node.next, node.pre
        self.dic.pop(node.key)

    def add(self, node):
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre.next = self.tail.pre = node
        self.dic[node.key] = node

    def __init__(self, capacity):
        self.dic = {}
        self.n = capacity
        self.head = self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key):
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1

    def put(self, key, value):
        if key in self.dic:
            self.remove(self.dic[key])
        node = Node(key, value)
        self.add(node)
        if len(self.dic) > self.n:
            self.remove(self.head.next)


class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.pre = None
