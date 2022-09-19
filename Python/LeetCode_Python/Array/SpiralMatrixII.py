#!/usr/bin/env python
# coding=utf-8
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        matrix = [[0 for _ in range(n)] for _ in range(n)]
        up, down, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        index = 1
        while True:
            for i in range(left, right + 1):
                matrix[up][i] = index
                index += 1
            up += 1
            if up > down:
                break
            for i in range(up, down + 1):
                matrix[i][right] = index
                index += 1
            right -= 1
            if right < left:
                break
            for i in range(right, left - 1, -1):
                matrix[down][i] = index
                index += 1
            down -= 1
            if down < up:
                break
            for i in range(down, up - 1, -1):
                matrix[i][left] = index
                index += 1
            left += 1
            if left > right:
                break
        return matrix


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        nums = [[0] * n for _ in range(n)]
        startx, starty = 0, 0               # 起始点
        loop, mid = n // 2, n // 2          # 迭代次数、n为奇数时，矩阵的中心点
        count = 1                           # 计数

        for offset in range(1, loop + 1) :      # 每循环一层偏移量加1，偏移量从1开始
            for i in range(starty, n - offset) :    # 从左至右，左闭右开
                nums[startx][i] = count
                count += 1
            for i in range(startx, n - offset) :    # 从上至下
                nums[i][n - offset] = count
                count += 1
            for i in range(n - offset, starty, -1) : # 从右至左
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, startx, -1) : # 从下至上
                nums[i][starty] = count
                count += 1
            startx += 1         # 更新起始点
            starty += 1

        if n % 2 != 0 :			# n为奇数时，填充中心点
            nums[mid][mid] = count
        return nums


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        res = [[0] * n for _ in range(n)]
        pos = [0, 0]
        move = (0, 1)
        for index in range(1, n * n + 1):
            res[pos[0]][pos[1]] = index
            if res[(pos[0] + move[0]) % n][(pos[1] + move[1]) % n] > 0:
                # (0, 1) -> (1, 0) -> (0, -1) -> (-1, 0)
                move = (move[1], -1 * move[0])
            pos[0] = pos[0] + move[0]
            pos[1] = pos[1] + move[1]
        return res
