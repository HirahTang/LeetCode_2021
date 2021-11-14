#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 15:21:34 2021

@author: hirahtang
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index0 = 0
        index1 = nums[0]
        inter = 0
        while index1 < len(nums) - 1:
#            print (index0, index1)
            if index0 == index1:
                return False
            for i in range(index0+1, index1 + 1):
                nums[i] = nums[i] + i
                inter = max(inter, nums[i])
            index0 = index1
            index1 = inter
            
        return True
            
            