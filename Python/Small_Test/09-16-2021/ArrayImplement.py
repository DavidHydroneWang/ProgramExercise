#!/usr/bin/env python
# coding=utf-8


class MyArray:

    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0

    def insert(self, index, element):
        #判断是否超出边界
        if index < 0 or index > self.size:
            raise Exception("超出数组边界")
        #从左到右，逐个右移
        for i in range(self.size-1, -1, -1):
            self.array[i+1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def output(self):
        for i in range(self.size):
            print(self.array[i])

    def insert_v2(self, index, element):
        if index < 0 or index > self.size:
            raise Exception("超出数组边界")
        if self.size >= len(self.array):
            self.resize()
        for i in range(self.size-1, -1, -1):
            self.array[i+1] = self.array[i]

        self.array[index] = element
        self.size += 1


    def resize(self):
        array_new = [None] * len(self.array) * 2
        for i in range(self.size):
            array_new[i] = self.array[i]
        self.array = array_new

    def remove(self, index):
        if index < 0 or index > self.size:
            raise Exception("超出数组边界")
        for i in range(index, self.size):
            self.array[i] = self.array[i+1]

        self.size -= 1





array = MyArray(4)
array.insert(0, 10)
array.insert(0, 11)
array.insert(0, 15)
array.insert_v2(0, 12)
array.insert_v2(0, 13)
array.insert_v2(0, 16)
array.remove(1)
array.output()
