# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 06:07:40 2020

@author: CeLiang
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans =0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                ans+=prices[i+1]-prices[i]
        return ans