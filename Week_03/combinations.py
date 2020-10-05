# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 05:48:46 2020

@author: CeLiang
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        num_list = []
        for i in range(1,n+1):
            num_list.append(int(i))
        ans = []
        def hepler(A, k, num_list):
            if len(A) == k:
                ans.append(list(A))
            else:
                for i in range(len(num_list)):
                    A.append(num_list[i])
                    hepler(A,k,num_list[i+1:])
                    A.pop()
            return ans
        return hepler([],  k, num_list)