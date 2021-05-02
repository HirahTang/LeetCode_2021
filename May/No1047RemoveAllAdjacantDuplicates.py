#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 18:55:45 2021

@author: hirahtang
"""

# =============================================================================
# 1047. Remove All Adjacent Duplicates In String
# =============================================================================

class Solution:
    def removeDuplicates(self, S):
        
        if len(S) == 1:
            return S
        
        queue = [0]
        for i in S:
            if i == queue[-1]:
                queue.pop(-1)
            else:
                queue.append(i)
            
        queue.pop(0)
        return ''.join(queue)