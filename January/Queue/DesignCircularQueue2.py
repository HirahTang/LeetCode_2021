#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 21:38:54 2021

@author: TH
"""
class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.q = [None] * k
        self.len = k
        self.front = 0
        self.rear = 0
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.q[self.rear] == None:
            self.q[self.rear] = value
            self.rear = (self.rear + 1) % self.len
            return True
        else:
            return False

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.q[self.front] == None:
            return False
        else:
            self.q[self.front] = None
            self.front = (self.front + 1) % self.len
            return True
        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        return  -1 if self.q[self.front] == None else self.q[self.front]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        return  -1 if self.q[self.rear - 1] == None else self.q[self.rear - 1]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.front == self.rear and self.q[self.front] == None
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.front == self.rear and self.q[self.front] != None