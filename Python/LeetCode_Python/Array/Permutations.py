#!/usr/bin/env python
# coding=utf-8
# no clue


from collections import deque
# Source:   https://tinyurl.com/s3ncxtn . This uses BFS to create all subsets of it's each levels.
class Solution(object):

    # Recursive solution
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        allPermutations = []
        self.generatePermutation(nums, 0, [], allPermutations)
        return allPermutations

    def generatePermutation(self, originalNums, currentIndex, runningPermutation, allPermutations):
        if currentIndex == len(originalNums):
            # finalPermutation = list(runningPermutation)
            allPermutations.append(runningPermutation)
        else:
            # create a new permutation by adding the current number at every position
            for idx in range(len(runningPermutation) + 1):
                newPermutation = list(runningPermutation)
                newPermutation.insert(idx, originalNums[currentIndex])
                self.generatePermutation(originalNums, currentIndex + 1, newPermutation, allPermutations)


    # Iterative solution
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        allPermutations = []
        currentPermutations = deque()
        currentPermutations.append([])
        for idx, currentNum in enumerate(nums):
            # we will take all existing permutations and add the current number to create new permutations
            currentPermutationsLength = len(currentPermutations)
            for _ in range(currentPermutationsLength):
                oldPermutation = currentPermutations.popleft()
                # create a new permutation by adding the current number at every position
                for position in range(len(oldPermutation) + 1):
                    newPermutation = list(oldPermutation)
                    newPermutation.insert(position, currentNum)
                    if len(newPermutation) == len(nums):
                        allPermutations.append(newPermutation)
                    else:
                        currentPermutations.append(newPermutation)
        return allPermutations


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutations = [[]]

        for num in nums:
            new_permutations = []
            for perm in permutations:
                for i in range(len(perm) + 1):
                    new_permutations.append(perm[:i] + [num] + perm[i:])
            permutations = new_permutations

        return permutations


class Solution:
    # import itertools
    # def permute(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     result = itertools.permutations(nums)
    #     result = [list(t) for t in result]
    #     return result

    def permute(self, nums):
        # DPS with swapping
        res = []
        if len(nums) == 0:
            return res
        self.get_permute(res, nums, 0)
        return res

    def get_permute(self, res, nums, index):
        if index == len(nums):
            res.append(list(nums))
            return
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            # s(n) = 1 + s(n-1)
            self.get_permute(res, nums, index + 1)
            nums[i], nums[index] = nums[index], nums[i]


class Solution2(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.permute_helper(nums, 0)

    def permute_helper(self, nums, index):

        permutations = []

        if index >= len(nums):
            permutations.append(nums[:])        # make a new copy to freeze nums

        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]     # swap with all indices >= index
            permutations += self.permute_helper(nums, index + 1)
            nums[i], nums[index] = nums[index], nums[i]     # swap back

        return permutations
