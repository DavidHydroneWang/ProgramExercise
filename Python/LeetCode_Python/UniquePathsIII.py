#!/usr/bin/env python
# coding=utf-8
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.steps = 0
        self.result = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 0:
                    self.steps += 1
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 1:
                    self.dfs(row + 1, col)
                    self.dfs(row - 1, col)
                    self.dfs(row, col + 1)
                    self.dfs(row, col - 1)
        return self.result

    def dfs(self, row, col, steps_count = 0):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols or self.grid[row][col] == -1:
            return
        elif self.grid[row][col] == 2 and steps_count == self.steps:
            self.result += 1
        elif self.grid[row][col] == 0:
            self.grid[row][col] = -1
            self.dfs(row + 1, col, steps_count + 1)
            self.dfs(row - 1, col, steps_count + 1)
            self.dfs(row, col + 1, steps_count + 1)
            self.dfs(row, col - 1, steps_count + 1)
            self.grid[row][col] = 0


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        unvisited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    start = (r, c)
                elif grid[r][c] == 2:
                    end = (r, c)
                    unvisited.add((r, c))
                elif grid[r][c] == 0:
                    unvisited.add((r, c))

        def make_paths(r, c):
            if not unvisited and (r, c) == end:     # end reached and no more cells to visit
                return 1
            if not unvisited or (r, c) == end:      # end reached with cells to visit or no more cells to visit
                return 0

            paths = 0
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nbor_r, nbor_c = r + dr, c + dc
                if (nbor_r, nbor_c) in unvisited:
                    unvisited.remove((nbor_r, nbor_c))
                    paths += make_paths(nbor_r, nbor_c)
                    unvisited.add((nbor_r, nbor_c)) # add back after exploring this path
            return paths

        return make_paths(*start)
