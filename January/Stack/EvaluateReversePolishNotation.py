#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 19:56:12 2021

@author: hirahtang
"""

# =============================================================================
# 150. Evaluate Reverse Polish Notation
# =============================================================================

class Solution:
    def evalRPN(self, tokens):
        
        calc = {
            "+", "-", "*", "/"
            }
        num_l = []
        for i in tokens:
            if i in calc:
                b = num_l.pop()
                a = num_l.pop()
                if i == '+':
                    res = a + b
                elif i == "-":
                    res = a - b
                elif i == "*":
                    res = a * b
                elif i == "/":
                    res = int(a / b)
                else:
                    continue
                num_l.append(res)
            else:
                num_l.append(int(i))
        return num_l[0]
        