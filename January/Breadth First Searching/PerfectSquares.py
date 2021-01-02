#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 19:49:59 2020

@author: TH
"""
class Solution:
    
    def queuerecursion(queue, num):
        
        
        
        size = len(queue)
        
        num += 1
        
        for i in range(size):
            
            init = 1
            while init ** 2 <= queue[i]:
                init += 1
            squares = set([i ** 2 for i in range(1, init)])
            
            for j in squares:
                new_item = queue[i] - j
                if new_item == 0:
                    return num
                else:
                    queue.append(new_item)
        for i in range(size):
            queue.pop(0)
        
        return Solution.queuerecursion(queue, num)
    
    def numSquares(self, n):
        # Firstly, we need to find the largest possible square number that forms up n
        num = 0
        
        queue = [n]
        
        return Solution.queuerecursion(queue, num)
        
        # queue = [n]
        # size = len(queue)
        # for number in range(size):
        
        #     for i in squares:
        #         if i
        