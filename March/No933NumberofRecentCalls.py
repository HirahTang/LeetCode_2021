#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 23:39:26 2021

@author: hirahtang
"""

# =============================================================================
# 933. Number of Recent Calls
# =============================================================================

class RecentCounter:

    def __init__(self):
        self.pings_l  =[]
        

    def ping(self, t: int):
        self.pings_l.append(t)
        self.pings_l = [time for time in self.pings_l if time > (t - 3001)]
        return len(self.pings_l)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)