'''
Insert In Stack
Difficulty: Basic
You are given an array arr[] of size N, the task is to insert the elements of the array into a stack from left to right

'''

class Solution:
    def InsertInStack(self,n,arr):
        stk=[]
        for i in arr[::-1]:
            stk.append(i)
        return arr

