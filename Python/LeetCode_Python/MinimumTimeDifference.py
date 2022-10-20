#!/usr/bin/env python
# coding=utf-8
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        res = []
        for i in range(1,len(timePoints)):
            res.append(self.Difference(timePoints[i], timePoints[i - 1]))
        res.append(self.Difference(timePoints[-1], timePoints[0]))
        return min(res)


    def Difference(self, time2, time1):
        h1, m1 = time1.split(':')
        h2, m2 = time2.split(':')
        res = int(m2) - int(m1)
        res += 60 * (int(h2) - int(h1))
        if res <= 779:
            return res
        else:
            return  1440 - res


class Solution:
    def changeTime(self, timePoint: str):
        hours, minutes = timePoint.split(':')
        return int(hours) * 60 + int(minutes)

    def findMinDifference(self, timePoints: List[str]) -> int:
        if not timePoints or len(timePoints) > 24 * 60:
            return 0

        times = sorted(self.changeTime(time) for time in timePoints)
        times.append(times[0] + 24 * 60)
        res = times[-1]
        for i in range(1, len(times)):
            res = min(res, times[i] - times[i - 1])
        return res
