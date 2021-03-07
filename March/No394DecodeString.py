#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 17:04:34 2021

@author: hirahtang
"""

# =============================================================================
# 394. Decode String
# =============================================================================

class Solution:
    def decodeString(self, s: str) -> str:
        cur_num = 0
        stack = []
        i = 0
        last_was_digit = False
        while i < len(s):
            ch = s[i]
            if ch.isdigit():
                cur_num = cur_num * 10 + int(ch)
                last_was_digit = True
            else:
                if last_was_digit:
                    stack.append(cur_num)
                    cur_num = 0
                    last_was_digit = False
                if ch == ']':
                    # Pop till left bracket
                    deq = deque([])
                    while stack[-1] != '[':
                        deq.appendleft(stack.pop())
                    # Remove the extra '['
                    stack.pop()
                    # Remove number of times to repeat
                    repeat = stack.pop()
                    # Append the current string
                    stack.extend(repeat * list(deq))
                else:
                    # Either [ or alphabet
                    stack.append(ch)
            i += 1
                        
        return "".join(stack)