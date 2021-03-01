#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 16:09:37 2021

@author: hirahtang
"""

# =============================================================================
# 1773. Count Items Matching a Rule
# =============================================================================

class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        if ruleKey == 'type':
            return sum([j == ruleValue for j in [i[0] for i in items]])
        elif ruleKey == 'color':
            return sum([j == ruleValue for j in [i[1] for i in items]])
        else:
            return sum([j == ruleValue for j in [i[2] for i in items]])
