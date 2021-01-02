#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 21:38:29 2021

@author: TH
"""
# =============================================================================
# Leetcode Problem
# No. 622 Design Circular Queue,
# =============================================================================



class MyCircularQueue:

    def __init__(self, k):
        self.k = k
        self.content = ['NA' for i in range(k)]
        self.head = 0
        self.tail = 0
        

    def enQueue(self, value):
        
        if self.isFull() == True:
            return False
        
        if self.isEmpty() == True:
            self.content[self.tail] = value
            return True
        
        else:
            # if self.content[self.tail] == False: 
            if self.tail == (self.k - 1):
                self.tail = 0
                self.content[self.tail] = value
                return True
            else:
                self.tail += 1
                self.content[self.tail] = value 
                return True


    def deQueue(self):
        
        if self.isEmpty() == True:
            return False
        else:
            self.content[self.head] = 'NA'
            if self.isEmpty() == True:
                return True
            else:
                if self.head == (self.k - 1):
                    self.head = 0
                    return True
                else:
                    self.head += 1
                    return True
            # if self.head == (len(self.head) - 1):
            #     self.head = 0
            # else:
            #     self.head += 1
            # return True

    def Front(self):
        
        if self.isEmpty() == True:
            return -1
        else:
            return self.content[self.head]
        
    def Rear(self):
        
        if self.isEmpty() == True:
            return -1
        else:
            return self.content[self.tail]

    def isEmpty(self):
        
        if self.tail == self.head and self.content[self.head] == 'NA':
            return True
        # for i in self.content:
        #     if i != 'NA':
        #         return False
        else:
            return False

    def isFull(self):
        
        # if self.tail == (self.head - 1):
        #     return True
        # if self.tail == (self.k- 1) and self.head == 0:
        #     return True
        # else:
        #     return False
        
        if 'NA' in self.content:
            return False
        else:
            return True