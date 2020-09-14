# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 02:28:39 2020

@author: CeLiang
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        for j in range(len(nums)):
            if nums[i]!=nums[j]:
                i+=1
                nums[i],nums[j] = nums[j],nums[i]        
        return i+1
