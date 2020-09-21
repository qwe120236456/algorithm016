# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 04:30:37 2020

@author: CeLiang
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict ={}
        for i in range(len(nums)):
            a, b =nums[i], target - nums[i]
            if b not in dict:
                dict[a] = i
            else:
                return(i,dict[b])