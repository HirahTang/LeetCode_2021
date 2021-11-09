#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 15:56:29 2021

@author: hirahtang
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(n ,s):
            while n < len(s) - 1:
                c = s.pop(0)
                s.insert(len(s) - n, c)
                n += 1
                return reverse(n, s)
            return s
        s = reverse(0, s)