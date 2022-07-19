#!/usr/bin/env python
# coding=utf-8


def merge(self, nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None
    """
    for i in range(n):
            nums1[m + i] = nums2[i]
    nums1.sort()
    return


def merge(self, nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None
    """
    nums1[m: m + n] = nums2[:n]
    for right in range(m, m + n):
        target = nums1[right]
        for left in range(0, right):
            if target <= nums1[left]:
                nums1[left + 1: right + 1] = nums1[left: right]
                nums1[left] = target
                break
    return
