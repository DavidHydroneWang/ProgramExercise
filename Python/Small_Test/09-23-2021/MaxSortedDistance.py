#!/usr/bin/env python
# coding=utf-8


class Bucket:
    def __init__(self):
        self.min = None
        self.max = None


def get_max_sorted_distance(array=[]):
    max_value = array[0]
    min_value = array[0]
    for i in range(1, len(array)):
        if array[i] > max_value:
            max_value = array[i]

        if array[i] < min_value:
            min_value = array[i]
    d = max_value - min_value
    if d == 0:
        return 0

    bucket_num = len(array)
    buckets = []
    for i in range(0, bucket_num):
        buckets.append(Bucket())
    for i in range(0, len(array)):
        index = int((array[i] - min_value) * (bucket_num-1) / d)
        if buckets[index].min is None or buckets[index].min > array[i]:
            buckets[index].min = array[i]

        if buckets[index].max is None or buckets[index].max < array[i]:
            buckets[index].max = array[i]
    left_max = buckets[0].max
    max_distance = 0
    for i in range(1, len(buckets)):
        if buckets[i].min is None:
            continue

        if buckets[i].min - left_max > max_distance:
            max_distance = buckets[i].min - left_max
        left_max = buckets[i].max

    return max_distance


my_array = list([2, 6, 3, 4, 5, 10, 9])
print(get_max_sorted_distance(my_array))
