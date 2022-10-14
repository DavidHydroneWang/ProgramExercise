#!/usr/bin/env python
# coding=utf-8
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prev = float('inf')
        for i in range(len(numbers)):
            #print(target - i)
            if prev ==  numbers[i]:
                continue
            if target - numbers[i] in numbers:
                start = i
                end = numbers.index(target - numbers[i],start + 1)
                res = [start + 1, end + 1]
                res.sort()
                return res
            else:
                prev = numbers[i]


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while True:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i + 1, j + 1]
