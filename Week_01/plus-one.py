# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 04:10:04 2020

@author: CeLiang
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans =0
        for i in range(len(digits)):
            ans = ans + digits[i] * (10** (len(digits)-i-1))
        ans = ans+1
        result=[]

        while (ans>0):
            tmp = ans% 10
            result.insert(0,tmp )
            ans = ans//10
        return result
