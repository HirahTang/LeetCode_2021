#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 17:55:36 2021

@author: hirahtang
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.normal_stack = []
        self.min_stack = []
        

    def push(self, x: int) -> None:
        if len(self.normal_stack) == 0:
            self.normal_stack.append(x)
            self.min_stack.append(x)
        else:
            self.min_stack.append(min(x, self.min_stack[-1]))
            self.normal_stack.append(x)
            
    def pop(self) -> None:
        if len(self.normal_stack) == 0:
            return
        self.normal_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if len(self.normal_stack) == 0:
            return -1
        else:
            return self.normal_stack[-1]

    def getMin(self) -> int:
        if len(self.normal_stack) == 0:
            return -1
        else:
            return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
