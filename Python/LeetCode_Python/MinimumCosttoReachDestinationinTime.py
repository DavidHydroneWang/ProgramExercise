#!/usr/bin/env python
# coding=utf-8
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        graph = [[] for _ in range(n)]

        minHeap = []
        cost = [math.inf] * n
        time = [math.inf] * n
        for x, y, t in edges:
            graph[x].append((y, t))
            graph[y].append((x, t))

        heapq.heappush(minHeap, (passingFees[0], 0, 0))
        cost[0] = passingFees[0]
        time[0] = 0

        while minHeap:
            currCost, currTime, x = heapq.heappop(minHeap)
            for y, pathTime in graph[x]:
                if currTime + pathTime <= maxTime:
                    # go from x -> y
                    newCost = currCost + passingFees[y]
                    newTime = currTime + pathTime
                    if cost[y] > newCost:
                        cost[y] = newCost
                        time[y] = newTime
                        heapq.heappush(minHeap, (newCost, newTime, y))
                    elif time[y] > newTime:
                        time[y] = newTime
                        heapq.heappush(minHeap, (newCost, newTime, y))

        return -1 if cost[-1] == math.inf else cost[-1]


class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        import collections
        import heapq

        adj = [[] for i in range(len(passingFees))]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        best = collections.defaultdict(lambda: float('inf'))

        best[0] = 0
        minHeap = [(passingFees[0], 0, 0)]

        while minHeap:
            result, u, w = heapq.heappop(minHeap)

            if w > maxTime:
                continue
            if u == len(passingFees) - 1:
                return result
            for v, nw in adj[u]:
                if w + nw < best[v]:
                    best[v] = w + nw
                    heapq.heappush(minHeap, (result + passingFees[v], v, w + nw))

        return -1
