#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 16:00:26 2021

@author: hirahtang
"""

class Solution:
    def totalMoney(self, n):
        output = 0
        weeks = int(n / 7)
        weeks = [i for i in range(1, weeks + 1)]
        for i in weeks:
            output += (i * 2 + 6) * 3.5
        resid = n % 7
        Mond = int(n / 7) + 1
        for i in range(resid):
            output += Mond
            Mond += 1
        return int(output)
        
                 