#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 17:47:26 2021

@author: hirahtang
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        
        self.stack.append(x)
        

    def pop(self):
        
        self.stack = self.stack[:-1]
        

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()