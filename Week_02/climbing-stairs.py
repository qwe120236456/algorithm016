# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 04:34:29 2020

@author: CeLiang
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2 :
            return n
        a, b = 1, 2
        for i in range(3,n+1):
            fn = a+ b
            a, b = b, a+b
            
            
        return fn
    