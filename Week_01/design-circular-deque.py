# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 05:14:26 2020

@author: CeLiang
"""
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.arr = [0 for _ in range(k)]
        self.maxi = k
        self.length =0
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.length < self.maxi:
    
            #tmp = self.arr[0:]
            #self.arr = [0 for _ in range(self.length+1)]
            self.arr[0],self.arr[1:] = value,self.arr[0:-1]
            self.length +=1
            return True
        else:
            return False
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.length < self.maxi:
            '''
            tmp = self.arr
            self.arr = [0 for _ in range(self.length+1)]
            self.arr[0:-1],self.arr[-1] = tmp,value
            '''
            self.arr[self.length] = value
            self.length +=1
            return True
        else:
            return False       

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if(self.length>0):
            tmp = self.arr
            self.arr[0:-1],self.arr[-1] = tmp[1:],0
            self.length-=1
            return True
        else:
            return False
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if(self.length>0):
            
            self.arr[self.length-1]=0
            self.length-=1
            return True
        else:
            return False
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if(self.length>0):
            return self.arr[0]
        else:
            return -1
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if(self.length>0):
            return self.arr[self.length-1]
        else:
            return -1     

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        if(self.length>0):
            return False
        else:
            return True    
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if(self.length==self.maxi):
            return True
        else:
            return False   

        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()