#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 25 13:52:31 2021

@author: hirahtang
"""

def func(n):
    start_n = 1
    while start_n ** 2 < n:
        start_n += 1
    if n == start_n ** 2:
        return 1
    select_l = []
    
    for i in range(1, start_n + 1):
        select_l.append(i ** 2)
    
    output = 0
    while n > 0:
        for i in select_l[::-1]:
            if n >= i:
                n -= i
                output += 1
                break
        if n == 0:
            return output


def func2(n):
    start_n = 1
    while start_n ** 2 < n:
        start_n += 1
    if n == start_n ** 2:
        return 1
    select_l = []
    
    for i in range(1, start_n + 1):
        select_l.append(i ** 2)
    
    queue = [[i, 1] for i in select_l]
    output = []
    while len(queue) > 0:
        current_comp = queue.pop(0)
        for j in select_l:
            new_value = current_comp[0] + j
            value_count = current_comp[1] + 1
            if new_value < n:
                queue.append([new_value, value_count])
                # queue.pop(0)
            elif new_value == n:
                output.append(value_count)
                # queue.pop(0)
            else:
                # queue.pop(0)
                continue
        
    return min(output)
    
# def bfs(queue, select_l, n):
#     for i in queue:
#         n -= i
        

# def func_bfs(n):
#     start_n = 1
#     while start_n ** 2 < n:
#         start_n += 1
#     if n == start_n ** 2:
#         return 1
#     select_l = []
    
#     for i in range(1, start_n + 1):
#         select_l.append(i ** 2)
    
#     output = 0
    
#     queue = []
#     for i in select_l[::-1]:
        