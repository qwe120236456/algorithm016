# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 06:20:37 2020

@author: CeLiang
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s):
            return False
        else:
            a = list(s)
            b = list(t)
            a.sort()
            b.sort()
            if a== b:
                return True
            else:
                return False

