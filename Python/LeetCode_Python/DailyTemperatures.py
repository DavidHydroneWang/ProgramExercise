#!/usr/bin/env python
# coding=utf-8
from collections import deque
class Solution: # 29 / 48 test cases passed. Status: Time Limit Exceeded
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        if all( i == temperatures[0] for i in temperatures):
            return res
        q = deque()
        for index, value in enumerate(temperatures):
            q.append((index, value))
        while True:
            try:
                temp = deque()
                old = q.popleft()
                new = q.popleft()
                #print(old, new)
                while new[1] <= old[1]:
                    #print(new)
                    temp.append(new)
                    if q:
                        new = q.popleft()
                    else:
                        new = None
                        break
                    #print(new)

                if new is not None:
                    temp.append(new)
                #print(temp)

                if new is None:
                    pass

                else:

                    res[old[0]] = new[0] - old[0]
                while temp:
                    q.appendleft((temp.pop()))

                #print(q)
            except Exception as e:
                #print(e)
                break
        return res



class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = []
        for index, value in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < value:
                j = stack.pop()
                res[j] = index - j
            stack.append(index)

        return res


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stk = []
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            while stk and temperatures[stk[-1]] <= temperatures[i]:
                stk.pop()
            if stk:
                ans[i] = stk[-1] - i
            stk.append(i)
        return ans



class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = [0]
        for i in range(1,len(temperatures)):
            # 情况一和情况二
            if temperatures[i]<=temperatures[stack[-1]]:
                stack.append(i)
            # 情况三
            else:
                while len(stack) != 0 and temperatures[i]>temperatures[stack[-1]]:
                    answer[stack[-1]]=i-stack[-1]
                    stack.pop()
                stack.append(i)

        return answer
