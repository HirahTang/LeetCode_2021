#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 15 22:11:40 2021

@author: hirahtang
"""

# =============================================================================
# 242. Valid Anagram
# =============================================================================

class Solution:
    def isAnagram(self, s, t):
        from collections import Counter
        return Counter(s) == Counter(t)


        