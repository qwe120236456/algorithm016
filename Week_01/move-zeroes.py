# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 04:09:28 2020

@author: CeLiang
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1

