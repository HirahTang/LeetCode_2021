#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 13:03:11 2021

@author: hirahtang
"""

# =============================================================================
# 88. Merge Sorted Array
# =============================================================================

from typing import List

# When we traverse the list, we start with the last elements (the largest one) and come back over
# So we would not need to worry about retaining elements in nums1 
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] < nums2[n - 1]:
                nums1[m + n -1] = nums2[n-1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m-1]
                m -= 1
        nums1[:n] = nums2[:n]
