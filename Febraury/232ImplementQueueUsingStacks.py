#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 21:04:51 2021

@author: hirahtang
"""

# =============================================================================
# 232. Implement Queue using Stacks
# =============================================================================

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.forwardstack = []
        self.reversestack = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        
        self.forwardstack.append(x)
        
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.reversestack) > 0:
            return self.reversestack.pop(-1)
        else:
            for i in range(len(self.forwardstack) - 1):
                self.reversestack.append(self.forwardstack.pop(-1))
            return self.forwardstack.pop(-1)

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.reversestack) > 0:
            return self.reversestack[-1]
        else:
            for i in range(len(self.forwardstack)):
                self.reversestack.append(self.forwardstack.pop(-1))
            return self.reversestack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return (len(self.forwardstack) + len(self.reversestack)) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()