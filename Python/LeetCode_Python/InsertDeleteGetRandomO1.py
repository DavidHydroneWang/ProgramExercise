#!/usr/bin/env python
# coding=utf-8
class RandomizedSet:

    def __init__(self):

        self.a = []
        self.m = {}


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.m:
            return False
        self.m[val] = len(self.a)
        self.a.append(val)
        return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.m:
            idx = self.m[val]
            self.a[idx], self.a[-1] = self.a[-1], self.a[idx]
            self.m[self.a[idx]] = idx
            self.a.pop()
            del self.m[val]
            return True
        else:
            return False


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.a)


import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already
        contain the specified element.
        """
        if val not in self.set:
            self.set.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the
        specified element.
        """
        if val in self.set:
            self.set.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.set)
