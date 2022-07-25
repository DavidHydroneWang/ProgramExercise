#!/usr/bin/env python
# coding=utf-8


class Node:
    def __init__(self, head):
        self.data = head
        self.next = None

    def getdata(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, new):
        self.data = new

    def setNext(self, nextdata):
        self.next = nextdata
