#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 22:14:10 2021

@author: hirahtang
"""

class Solution:
    def minSubArrayLen(self, target, nums):
        
        if sum(nums) < target:
            return 0
        elif sum(nums) == target:
            return len(nums)
        
        output = len(nums)+1
        pointer = 0
        
        continuous_l = []
        
        while pointer <= len(nums):
            # print (pointer, continuous_l)
            if sum(continuous_l) < target:
                if pointer  == len(nums):
                    break
                else:
                    continuous_l.append(nums[pointer])
                    pointer += 1

            elif sum(continuous_l) >= target:
                # output.append(len(continuous_l))
                output = min(output, len(continuous_l))
                continuous_l.pop(0)

        if output == len(nums) + 1:
            return 0
        else:
            return output
        
