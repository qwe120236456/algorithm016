# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 06:55:51 2020

@author: CeLiang
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ams =[]
        def helper(root,ans =[]):
            if root:
                helper(root.left,ans)
                ans.append(root.val)
                helper(root.right,ans)
            return ans
        ams = helper(root)
        return ams
