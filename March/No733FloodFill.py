#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 18:19:16 2021

@author: hirahtang
"""

# =============================================================================
# 733. Flood Fill
# =============================================================================

class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor):
        
        def DFSfill(stack, image, newColor, oldColor):
            coord = stack.pop()
            if coord[0] + 1 <= len(image) - 1:
                if image[coord[0] + 1][coord[1]] == oldColor:
                    image[coord[0] + 1][coord[1]] = newColor
                    stack.append((coord[0] + 1, coord[1]))
                    # print (coord[0] + 1,coord[1])
            if coord[0] - 1 >= 0:
                if image[coord[0] - 1][coord[1]] == oldColor:
                    image[coord[0] - 1][coord[1]] = newColor
                    # print (coord[0] - 1,coord[1])
                    stack.append((coord[0] - 1, coord[1])) 
            if coord[1] + 1 <= len(image[0]) - 1:
                if image[coord[0]][coord[1] + 1] == oldColor:
                    image[coord[0]][coord[1] + 1] = newColor
                    # print (coord[0],coord[1] + 1)
                    stack.append((coord[0], coord[1] + 1))
            if coord[1] - 1 >= 0:
                if image[coord[0]][coord[1] - 1] == oldColor:
                    image[coord[0]][coord[1] - 1] = newColor
                    # print (coord[0],coord[1] - 1)
                    stack.append((coord[0], coord[1] - 1))
            if stack == []:
                return image
            else:
                return DFSfill(stack, image, newColor, oldColor)
            
        oldColor = image[sr][sc]
        image[sr][sc] = newColor
        if oldColor == newColor:
            return image
        # print (oldColor)
        return DFSfill([(sr, sc)], image, newColor, oldColor)
            
        