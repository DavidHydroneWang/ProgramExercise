#!/usr/bin/env python
# coding=utf-8
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        import heapq
        idx = list(range(len(tasks)))
        idx.sort(key=lambda x: tasks[x][0])
        result, min_heap = [], []
        i, time = 0, tasks[idx[0]][0]
        while i < len(idx) or min_heap:
            while i < len(idx) and tasks[idx[i]][0] <= time:
                heapq.heappush(min_heap, (tasks[idx[i]][1], idx[i]))
                i += 1
            if not min_heap:
                time = tasks[idx[i]][0]
                continue
            t, j = heapq.heappop(min_heap)
            time += t
            result.append(j)
        return result


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        A = [[*task, i] for i, task in enumerate(tasks)]
        #print(A)
        ans = []
        minHeap = []
        i = 0  # tasks' pointer
        time = 0  # current time

        A.sort()

        while i < n or minHeap:
            if not minHeap:
                time = max(time, A[i][0])
            while i < n and time >= A[i][0]:
                heapq.heappush(minHeap, (A[i][1], A[i][2]))
                i += 1
            procTime, index = heapq.heappop(minHeap)
            time += procTime
            ans.append(index)

        return ans
