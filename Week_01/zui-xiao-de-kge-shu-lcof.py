# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 06:29:23 2020

@author: CeLiang



十分抱歉这周时间紧张 这道题用了划水的办法 后面会补上正规解法的
"""
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]