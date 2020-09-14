# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 04:04:05 2020

@author: CeLiang
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(len(nums)):
            a,b=nums[i], target-nums[i]
            if b not in dict.keys() :
                dict[a] = i
            else:
                return i,dict[b]