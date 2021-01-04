#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 18:12:44 2021

@author: hirahtang
"""

class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')',
         '[':']',
         '{':'}'
         }
        stack = []
        for i in s:
            if i in d:
                stack.append(d[i])
            elif i in stack:
                out = stack.pop()
                if out != i:
                    return False
            else:
                return False
        return stack == []