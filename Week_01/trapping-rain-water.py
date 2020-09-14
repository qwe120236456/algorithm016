# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 07:40:31 2020

@author: CeLiang
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        #dict={}
        ans =0

        for i in range(1,len(height)-1):
            l_max = max(height[0:i])
            r_max = max(height[i+1:])
            min_height = min(l_max, r_max)
            if min_height>height[i]:
                ans = ans+min_height-height[i]

        return ans