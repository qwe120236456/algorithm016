# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 02:46:16 2020

@author: CeLiang
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(k):
            nums.insert(0, nums.pop())
        
            
