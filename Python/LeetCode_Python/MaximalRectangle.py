#!/usr/bin/env python
# coding=utf-8
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        ans = 0
        hist = [0] * len(matrix[0])

        def largestRectangleArea(heights: List[int]) -> int:
            ans = 0
            stack = []

            for i in range(len(heights) + 1):
                while stack and (i == len(heights) or heights[stack[-1]] > heights[i]):
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1 if stack else i
                    ans = max(ans, h * w)
                stack.append(i)

            return ans

        for row in matrix:
            for i, num in enumerate(row):
                 hist[i] = 0 if num == '0' else hist[i] + 1
            ans = max(ans, largestRectangleArea(hist))

        return ans


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        max_area = 0
        heights = [0] * cols

        for row in range(rows):

            heights = [heights[i]+1 if matrix[row][i]=='1' else 0 for i in range(cols)]
            heights.append(0)
            stack = [0]

            for col in range(1, len(heights)):
                while stack and heights[col] < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    if not stack:
                        width = col
                    else:
                        width = col - stack[-1] - 1
                    max_area = max(max_area, height * width)

                stack.append(col)

        return max_area


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        heights = [0 for _ in matrix[0]]
        maxRect = float('-inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == "0":
                    heights[j] = 0
                else:
                    heights[j] += 1
            maxRect = max(maxRect, self.largestRectangleArea(heights))
        return maxRect


    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1]
        finalArea = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                finalArea = max(finalArea, height *width)
            stack.append(i)
        heights.pop()
        return finalArea
