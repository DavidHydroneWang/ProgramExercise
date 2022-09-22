#!/usr/bin/env python
# coding=utf-8
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        length = len(s)
        res = []
        for i in range(1, length):
            for j in range(1, length):
                for k in range(1, length):
                    #for l in range(1, length):
                    if  0 < j - i <= 3 and 0 < k - j <= 3:
                        res.append(s[:i ] + '.' + s[i : j] + '.' + s[j:k] + '.' + s[k:] )
        result = []
        for ip in  res:
            if self.validIP(ip):
                result.append(ip)
        return result


    def validIP(self, s):
        l = s.split('.')
        for i in l:
            if  int(i) < 0 or int(i) > 255 or (len(i) > 1 and i[0] == '0'):
                return False
        return True


class Solution:
    result = []
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.result.clear()
        if len(s) > 12: return []
        self.backtracking(s, 0, 0)
        return self.result

    def backtracking(self, s: str, start_index: int, point_num: int) -> None:
        # Base Case
        if point_num == 3:
            if self.is_valid(s, start_index, len(s)-1):
                self.result.append(s[:])
            return
        # 单层递归逻辑
        for i in range(start_index, len(s)):
            # [start_index, i]就是被截取的子串
            if self.is_valid(s, start_index, i):
                s = s[:i+1] + '.' + s[i+1:]
                self.backtracking(s, i+2, point_num+1)  # 在填入.后，下一子串起始后移2位
                s = s[:i+1] + s[i+2:]    # 回溯
            else:
                # 若当前被截取的子串大于255或者大于三位数，直接结束本层循环
                break

    def is_valid(self, s: str, start: int, end: int) -> bool:
        if start > end: return False
        # 若数字是0开头，不合法
        if s[start] == '0' and start != end:
            return False
        if not 0 <= int(s[start:end+1]) <= 255:
            return False
        return True


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def dfs(start: int, path: List[int]) -> None:
            if len(path) == 4 and start == len(s):
                ans.append(path[0] + '.' + path[1] + '.' + path[2] + '.' + path[3])
                return
            if len(path) == 4 or start == len(s):
                return

            for length in range(1, 4):
                if start + length > len(s):
                    return  # out of bound
                if length > 1 and s[start] == '0':
                    return  # leading '0'
                num = s[start: start + length]
                if int(num) > 255:
                    return
                dfs(start + length, path + [num])

        dfs(0, [])
        return ans

class Solution:
    # result = []
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12: return []
        bfs = [(0, '')]
        for c in s:
            new = []
            c = int(c)
            for cur, st in bfs:
                if cur * 10 + c <= 255 and (st[-1:] != '0' or cur):
                    new.append((cur * 10 + c, st + str(c)))
                if st:
                    new.append((c, st + '.' + str(c)))
            bfs = new
        return [st for cur, st in bfs if st.count('.') == 3]
