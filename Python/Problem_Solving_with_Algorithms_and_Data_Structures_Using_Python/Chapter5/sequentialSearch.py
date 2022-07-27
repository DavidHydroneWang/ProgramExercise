#!/usr/bin/env python
# coding=utf-8


def sequentialSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            return True
        else:
            pos += 1
    return found
