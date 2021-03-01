#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 16:34:15 2021

@author: hirahtang
"""

# =============================================================================
# 1774. Closest Dessert Cost
# =============================================================================

# class Solution:
#     def closestCost(self, baseCosts, toppingCosts, target):
#         toppingCosts = sorted(toppingCosts)
#         baseCosts = sorted(baseCosts)
#         output = 0
#         # combinations = []
#         for i in baseCosts:
#             combinations = [i]
#             diff = abs(target - sum(combinations))

#             if i >= target:
#                 return i
            
#             for j in toppingCosts[::-1]:
#                 combinations.append(j)
#                 if sum(combinations) > target:
#                     if abs(target - sum(combinations)) < diff:
#                         output = sum(combinations)

import itertools

# =============================================================================
# Greedy, BackTracking, Brute Force
# =============================================================================

class Solution:
    def closestCost(self, baseCosts, toppingCosts, target):
        res = 1e4
        for bc in baseCosts:
            it_tc = itertools.product([0, 1, 2], repeat=len(toppingCosts)) # new iterator every time
            for it in it_tc:
                tmp = bc + sum([tc * n for n, tc in zip(it, toppingCosts)])
                if abs(tmp - target) < abs(res - target):
                    res = tmp
        return res
            
            
            
            
            
        