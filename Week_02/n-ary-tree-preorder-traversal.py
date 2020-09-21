# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 04:28:33 2020

@author: CeLiang
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def helper(root,ans=[]):
            if root:
                ans.append(root.val)
                children = root.children
                for child in children:
                    helper(child,ans)
            return ans
        return helper(root)