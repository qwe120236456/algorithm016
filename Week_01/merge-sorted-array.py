# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 03:06:03 2020

@author: CeLiang
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0:
            nums1=nums1[0:m]
        if m==0:
            nums1[:] = nums2[:]    
        elif m!=0 and n!=0:
            nums1[-n:]=nums2
        nums1.sort()