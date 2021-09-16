#!/usr/bin/env python
# coding=utf-8


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.last = None

    def get(self, index):
        if index < 0 or index >= self.size:
            raise Exception("超出链表范围")
        p = self.head
        for i in range(index):
            p = p.next
        return p

    def insert(self, data, index):
        if index < 0 or index > self.size:
            raise Exception("超出链表范围")
        node = Node(data)
        if self.size == 0:
            self.head = node
            self.last = node
        elif index == 0:
            node.next = self.head
            self.head = node
        elif self.size == index:
            self.last.next = node
            self.last = node
        else:
            prev_node = self.get(index-1)
            node.next = prev_node.next
            prev_node.next = node
        self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise Exception("超出链表范围")
        if index == 0:
            remove_node = self.head
            self.head = self.head.next
        elif index == self.size - 1:
            prev_node = self.get(index-1)
            remove_node = prev_node.next
            prev_node.next = None
            self.last = prev_node

        else:
            prev_node = self.get(index-1)
            next_node = prev_node.next.next
            remove_node = prev_node.next
            prev_node.next = next_node
            self.size -= 1
            return remove_node

    def output(self):
        p = self.head
        while p is not None:
            print(p.data)
            p = p.next


linkedList = LinkedList()
linkedList.insert(3, 0)
linkedList.insert(4, 0)
linkedList.insert(9, 2)
linkedList.insert(6, 3)
linkedList.insert(6, 1)
linkedList.remove(0)
linkedList.output()
