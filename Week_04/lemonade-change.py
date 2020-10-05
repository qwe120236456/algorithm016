# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 06:05:48 2020

@author: CeLiang
"""
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        box_5 = 0
        box_10 =0
        for money in bills:
            if money == 5:
                box_5 += 5
            elif money == 10:
                box_5 -= 5
                box_10 += 10
            elif money ==20:
                if box_10 >= 10:
                    box_10 -=10
                    box_5-=5
                else:
                    box_5-=15
            if box_5<0 or box_10<0:
                return False

        return True