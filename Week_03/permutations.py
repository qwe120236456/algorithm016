# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 06:02:40 2020

@author: CeLiang
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(A =[],n=len(nums),ans=[],num_list=nums):
            if len(A)==n:
                ans.append(list(A))
            else:
                for d in num_list:
                    A.append(d)
                    tmp = num_list.copy()
                    tmp.remove(d)
                    helper(A=A,num_list=tmp)
                    A.pop()
            return ans 
        return helper()