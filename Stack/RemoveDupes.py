'''
Removing consecutive duplicates
Difficulty: Easy
You are given string s. You need to remove the consecutive duplicates from the given string using a Stack.  
'''
class Solution:
    
    #Function to remove consecutive duplicates from given string using Stack.
    def removeConsecutiveDuplicates(self,s):
        stk=[]
        for i in s:
            if not stk:
                stk.append(i)
            else:
                if stk[-1]!=i:
                    stk.append(i)
        return "".join(stk)
                