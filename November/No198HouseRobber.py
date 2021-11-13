#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 22:25:13 2021

@author: hirahtang
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
#        rob = nums.copy()
        for i in range(len(nums)):
            if i <= 1:
                continue
            nums[i] = nums[i] + max(nums[:i-1])
        return max(nums)