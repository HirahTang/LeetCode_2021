#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 21:39:20 2021

@author: TH
"""
class MyCircularQueue(object):

    def __init__(self, k):
        self.queue = list()
        self.cur = 0
        self.k = k
        
    def enQueue(self, value):
        if self.cur != self.k:
            self.cur += 1
            self.queue.append(value)
            return True
        else:
            return False
        
    def deQueue(self):
        if self.cur:
            self.cur -= 1
            self.queue.pop(0)
            return True
        else:
            return False

    def Front(self):
        if self.cur:
            return self.queue[0]
        else:
            return -1

    def Rear(self):
        if self.cur:
            return self.queue[-1]        
        else:
            return -1
        
    def isEmpty(self):
        if self.cur:
            return False
        else:
            return True

    def isFull(self):
        if self.cur == self.k:
            return True
        else:
            return False