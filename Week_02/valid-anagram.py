# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 04:25:44 2020

@author: CeLiang
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 ={}
        dict2 ={}
        if len(s) !=len(t):
            return False
        else:
            for i in range(len(s)):
                dict1[s[i]] = dict1.get(s[i],0) +1
                dict2[t[i]] = dict2.get(t[i],0) +1
            return dict1 == dict2