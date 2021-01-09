#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 14:47:08 2021

@author: hirahtang
"""

# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if len(tinput) < k or k <= 0:
            return []
        orig = sorted(tinput[:k])
        for i in tinput[k:]:
            if i < max(orig):
                orig.pop(-1)
                orig.append(i)
                orig = sorted(orig)
            else:
                continue
        return orig