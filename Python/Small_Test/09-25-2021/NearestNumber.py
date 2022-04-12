#!/usr/bin/env python
# coding=utf-8


def find_nearset_number(numbers=[]):
    index = find_transfer_point(numbers)
    if index == 0:
        return None
    numbers_copy = numbers.copy()
    exchange_head(index, numbers_copy)
    reverse(index, numbers_copy)
    return numbers_copy


def find_transfer_point(numbers=[]):
    for i in range(len(numbers)-1, 0, -1):
        if numbers[i] > numbers[i-1]:
            return 1

    return 0

def exchange_head(index, numbers=[]):
    head = numbers[index-1]
    for i in range(len(numbers)-1, 0, -1):
        if head < numbers[i]:
            numbers[index-1] = numbers[i]
            numbers[i] = head
            break
    return numbers

def reverse(index, numbers=[]):
    i = index
    j = len(numbers) -1
    while i < j:
        temp = numbers[i]
        numbers[i] = numbers[j]
        numbers[j] = temp
        i += 1
        j -= 1
    return numbers

def output_numbers(numbers=[]):
    for i in numbers:
        print(i, end='')
    print()


my_numbers = list([1, 2, 3, 4, 5])
for k in range(0, 10):
    my_numbers = find_nearset_number(my_numbers)
    output_numbers(my_numbers)
