#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 21:47:51 2021

@author: hirahtang
"""

# =============================================================================
# 225. Implement Stack using Queues
# =============================================================================
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []
        

    def push(self, x: int):
        """
        Push element x onto stack.
        """
        self.queue1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        """
        if len(self.queue1) == 1:
            return self.queue1.pop(0)
        elif len(self.queue1) > 1:
            for i in range(len(self.queue1) - 1):
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop(0)
        elif len(self.queue1) == 0:
            for i in range(len(self.queue2) - 1):
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        
        if len(self.queue1) == 1:
            top = self.queue1.pop(0)
            self.queue1.append(top)
            return top
        elif len(self.queue1) > 1:
            for i in range(len(self.queue1) - 1):
                self.queue2.append(self.queue1.pop(0))
            top = self.queue1.pop(0)
            self.queue2.append(top)
            return top
        elif len(self.queue1) == 0:
            for i in range(len(self.queue2) - 1):
                self.queue1.append(self.queue2.pop(0))
            top = self.queue2.pop(0)
            self.queue1.append(top)
            return top

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue1) + len(self.queue2) == 0 


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()