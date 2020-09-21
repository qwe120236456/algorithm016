# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 04:31:47 2020

@author: CeLiang
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict ={}
        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            if key not in dict:
                dict[key] = [strs[i]]
            else:
                dict[key].append(strs[i])
        return list(dict.values())