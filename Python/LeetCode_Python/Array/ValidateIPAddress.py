#!/usr/bin/env python
# coding=utf-8
class Solution:
    def solve(self , IP: str) -> str:
        # write code here
        flag = 'Neither'
        if '.' in IP:
            list1 = IP.split('.')
            if len(list1) == 4:
                for group in list1:
                    #print(group)
                    if not group:
                        return "Neither"
                    try:
                        n = int(group)
                        if n < 0 or n > 255 or len(str(n)) != len(group):
                            return "Neither"
                    except Exception as e:
                        return "Neither"
                return "IPv4"
            else:
                return "Neither"
        elif ':' in IP:
            list1 = IP.split(':')
            if len(list1) != 8:
                return "Neither"
            else:
                for group in list1:
                    if not group:
                        return "Neither"
                    try:
                        n = int(group, 16)
                        if n < 0 or n > int('FFFF', 16) or len(group) > 4 or group[0] == '-':
                            return "Neither"
                    except Exception as e:
                        return "Neither"
                return "IPv6"
        return "Neither"


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        ip4, ip6 = queryIP.split("."), queryIP.split(":")
        if len(ip4) == 4:
            for num in ip4:
                try:
                    if not (num[0] in string.digits and int(num) < 256 and (num[0] != "0" or num == "0")): return "Neither"
                except: return "Neither"
            return "IPv4"
        elif len(ip6) == 8:
            for num in ip6:
                try:
                    if not (num[0] in string.hexdigits and 0 <= int(num, 16) and len(num) <= 4): return "Neither"
                except: return "Neither"
            return "IPv6"
        return "Neither"
