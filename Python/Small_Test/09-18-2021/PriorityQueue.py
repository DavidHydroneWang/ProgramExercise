#!/usr/bin/env python
# coding=utf-8


class PriorityQueue:
    #  二叉堆的最大堆
    def __init__(self):
        self.array = []
        self.size = 0


    def enqueue(self, element):
        self.array.append(element)
        self.size += 1
        self.up_adjust()


    def dequeue(self):
        if self.size < 0:
            raise Exception("队列为空！")
        head = self.array[0]
        self.array[0] = self.array[self.size-1]
        self.size -= 1
        self.down_adjust()
        return head


    def up_adjust(self):
        child_index = self.size - 1
        parent_index = (child_index - 1) // 2
        temp = self.array[child_index]
        while child_index > 0 and temp > self.array[parent_index]:
            self.array[child_index] = self.array[parent_index]
            child_index = parent_index
            parent_index = (child_index - 1) // 2
        self.array[child_index] = temp


    def down_adjust(self):
        parent_index = 0
        temp = self.array[parent_index]
        child_index = 1
        while child_index < self.size:
            if child_index + 1 < self.size and self.array[child_index + 1] \
               > self.array[child_index]:
                child_index += 1
            if temp >= self.array[child_index]:
                break

            self.array[parent_index] = self.array[child_index]
            parent_index = child_index
            child_index = 2 * parent_index + 1
        self.array[parent_index] = temp


queue = PriorityQueue()
queue.enqueue(3)
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(2)
queue.enqueue(7)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
