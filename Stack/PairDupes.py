'''
Removing consecutive duplicates - 2
Difficulty: Easy
You are given string s. You need to remove the pair of duplicates.
Note: The pair should be of adjacent elements and after removing a pair the remaining string is joined together. 
'''
class Solution:
    
    #Function to remove pair of duplicates from given string using Stack.
    def removePair(self,s):
        stk=[]
        for i in s:
            if not stk:
                stk.append(i)
            else:
                if stk[-1]==i:
                    stk.pop()
                else:
                    stk.append(i)
        if stk:
            return "".join(stk)
        return "Empty String"
