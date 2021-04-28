#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 15:38:53 2021

@author: hirahtang
"""

# =============================================================================
# 29. Divide Two Integers
# =============================================================================

class Solution:
    
    def div_f(dividend, divisor):
        n = 0
        while dividend >= divisor:
            dividend -= divisor
            n += 1
        if n > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return n
    
    def divide(self, dividend, divisor):
        
        if dividend > 2 ** 31 - 1:
            return 2 ** 31 - 1
        
        if dividend * divisor >= 0: # Divident and divisor are of the same valuence
            if divisor < 0:
                return Solution.div_f(abs(dividend), abs(divisor))
            else:
                return Solution.div_f(dividend, divisor)
        else: # Divident and divisor are of the different valuence
            return Solution.div_f(abs(dividend), abs(divisor)) * (-1)