#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 21:30:04 2021

@author: hirahtang
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        out_str = [root]
        def bfs_str_create(queue, output):
            new_queue = []
            if not queue:
                return output
            for node in queue:
                if node:
                    new_queue.append(node.left)
                    new_queue.append(node.right)
            output.extend(new_queue)
            return bfs_str_create(new_queue, output)
        serial =  bfs_str_create(out_str, out_str)
        out_str = []
        for i in serial:
            if i:
                out_str.append(i.val)
            else:
                out_str.append(None)
        print(out_str)
        return ','.join([str(i) for i in out_str])
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        
        def buildTree(data, c_layer):
            if not data:
                return root
            new_c_layer = []
            for i in range(len(c_layer)):
                if c_layer[i].val or c_layer[i].val == 0:
                    c_value = data.pop(0)
                    if c_value or c_value ==0:
                        c_layer[i].left = TreeNode(c_value)
                        new_c_layer.append(c_layer[i].left)
                    c_value = data.pop(0)
                    if c_value or c_value == 0:
                        c_layer[i].right = TreeNode(c_value)
                        new_c_layer.append(c_layer[i].right)
            return buildTree(data, new_c_layer)
        
        data = data.split(',')
        for i in range(len(data)):
            try:
                data[i] = int(data[i])
            except:
                data[i] = None
        root = TreeNode(data.pop(0))
        if root.val or root.val == 0:
            return buildTree(data, [root])
        else:
            return []


# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
l_ = '4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2,None,None,None,None,None,None,None'
deser.deserialize(l_)
# ans = deser.deserialize(ser.serialize(root))