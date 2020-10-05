# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 06:09:41 2020

@author: CeLiang
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        energy =1
        for i in range(len(nums)-1):
            energy -=1
            energy = max(energy, nums[i])
            if energy ==0:
                return False
        return True