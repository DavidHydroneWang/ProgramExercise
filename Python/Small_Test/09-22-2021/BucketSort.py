#!/usr/bin/env python
# coding=utf-8


def bucket_sort(array=[]):
    max_value = array[0]
    min_value = array[0]
    for i in range(1, len(array)):
        if array[i] > max_value:
            max_value = array[i]

        if array[i] < min_value:
            min_value = array[i]
    d = max_value - min_value
    bucket_num = len(array)
    bucket_list = []
    for i in range(0, bucket_num):
        bucket_list.append([])

    for i in range(0, len(array)):
        num = int((array[i] - min_value) * (bucket_num-1) / d)
        bucket = bucket_list[num]
        bucket.append(array[i])

    for i in range(0, len(bucket_list)):
        bucket_list.sort()

    sorted_array = []
    for sub_list in bucket_list:
        for element in sub_list:
            sorted_array.append(element)
    return sorted_array


my_array = list([4.12, 6.421, 0.0023, 3.0, 2.123, 8.122, 4.12, 10.09])
print(bucket_sort(my_array))
