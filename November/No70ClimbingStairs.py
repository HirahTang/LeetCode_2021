#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 00:09:22 2021

@author: hirahtang
"""

class Solution:
    def climbStairs(self, n: int) -> int: # Top down with memory
        def helper(n, save_dict):
            if n in save_dict:
                return save_dict[n]
            return helper(n-1, save_dict) + helper(n-2, save_dict)
        save_dict = {0:0, 1:1, 2:2}
        ind_ = 0
        while ind_ < n:
            ind_ += 1
            save_dict[ind_] = helper(ind_, save_dict)
        return save_dict[n]
            
    def climbStairs2(self, n): # Climb up
        res, pre = 1, 1
        for i in range(2, n+1):
            res, pre = pre, res + pre
        return pre