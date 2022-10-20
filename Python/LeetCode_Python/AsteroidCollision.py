#!/usr/bin/env python
# coding=utf-8
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if len(asteroids) < 2:
            return asteroids
        if len(asteroids) == 2:
            if asteroids[0] * asteroids[1] < 0 and asteroids[0] > 0:
                if abs(asteroids[0]) == abs(asteroids[1]):
                    return []
                elif abs(asteroids[0]) > abs(asteroids[1]):
                    return [asteroids[0]]
                else:
                    return [asteroids[1]]
            else:
                return asteroids
        res = []
        for i in range(len(asteroids) - 1):

            if asteroids[i] * asteroids[i + 1] < 0 and asteroids[i] > 0:
                if abs(asteroids[i]) == abs(asteroids[i + 1]):
                    return self.asteroidCollision(asteroids[:i] + asteroids[i + 2:])
                elif abs(asteroids[i]) < abs(asteroids[i + 1]):
                    return self.asteroidCollision(asteroids[:i] + asteroids[i + 1:])
                else:
                    return self.asteroidCollision(asteroids[:i + 1] + asteroids[i + 2:])
        return asteroids


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for a in asteroids:
            if a > 0:
                ans.append(a)
            else:
                while len(ans) > 0 and ans[-1] > 0 and ans[-1] < -a:
                    ans.pop()
                if len(ans) > 0 and ans[-1] == -a:
                    ans.pop()
                elif len(ans) == 0 or ans[-1] < -a:
                    ans.append(a)

        return ans


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if not stack or asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and 0 < stack[-1] < -asteroid:
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(asteroid)
                elif stack[-1] == -asteroid:
                    stack.pop()

        return stack
