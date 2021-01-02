#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 21:37:21 2021

@author: TH
"""
class Solution:
    
    def panel(state, target, deadends, queue): # A function which to know new states from the given state
        
        for i in range(4):
            new1 = [j for j in state]
            new2 = [j for j in state]
            new1[i] = (new1[i] + 1) % 10
            new1 = ''.join(list(map(str, new1)))
            
            
           
            new2[i] = (new2[i] + 9) % 10
            new2 = ''.join(list(map(str, new2)))
            # print (new1, new2)
            if new2 not in deadends:
                queue.append(new2)
                deadends.add(new2)
            if new1 not in deadends:
                queue.append(new1)
                deadends.add(new1)
        # print ('added:', new_states)
        
        return queue, deadends
        
    
    def bfs(queue, target, deadends, steps):
        # print ('In queue:', queue)
        # print ('Deadends:', deadends)
        
        steps += 1
        size = len(queue)
        # for i in queue:
        #     deadends.append(i)
        new_queue = []
        for i in range(size):
            cur = list(map(int, list(queue[i])))
            new_queue, deadends = Solution.panel(cur, target, deadends, new_queue)
        # print (new_queue)
        for j in new_queue:
            queue.append(j)
        for i in range(size):
            queue.pop(0)
        if target in queue:
            # print (steps)
            # print ('In queue:', queue)
            return steps
        
        elif len(queue) == 0:
            return -1
        
        else:
            return Solution.bfs(queue, target, deadends, steps)
                

    def openLock(self, deadends, target):
        steps = 0
        
        deadends = set(deadends)
        
        if target == '0000':
            return steps
        if '0000' in deadends:
            return -1
        
        output =  Solution.bfs(['0000'], target, deadends, steps)
        
        
        return (output)