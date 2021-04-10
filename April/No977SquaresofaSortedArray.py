#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 16:13:59 2021

@author: hirahtang
"""

# =============================================================================
# 977. Squares of a Sorted Array
# =============================================================================

class Solution:
    def sortedSquares(self, nums):
        output = []
        left, right = 0, len(nums) - 1
        while left <= right:
            cur_l = nums[left] ** 2
            cur_r = nums[right] ** 2
            if cur_l > cur_r:
                output.append(cur_l)
                left += 1
            else:
                output.append(cur_r)
                right -= 1
        return output[::-1]
        