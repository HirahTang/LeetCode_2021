#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 23:28:34 2021

@author: hirahtang
"""

# =============================================================================
# 53. Maximum Subarray
# =============================================================================
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        output = nums[0]
        for i in range(1, len(nums)):
            current = max((nums[i] + dp[i-1]), nums[i])
            dp.append(current)
            output = max(output, current)
        return output

