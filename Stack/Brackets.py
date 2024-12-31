'''
Parenthesis Checker
Difficulty: Easy
You are given a string s representing an expression containing various types of brackets: {}, (), and []. Your task is to determine whether the brackets in the expression are balanced. A balanced expression is one where every opening bracket has a corresponding closing bracket in the correct order.
'''
class Solution:
    #Function to check if brackets are balanced or not.
    def isParenthesisBalanced(self, s):
        stk=[]
        for i in s:
            if not stk:
                stk.append(i)
            elif i=='(' or i=="{" or i=="[":
                stk.append(i)
            else:
                if i==')' and stk[-1]=="(" or i=='}' and stk[-1]=="{" or i==']' and stk[-1]=="[":
                    stk.pop()
                else:
                    return False
        if not stk:
            return True
        else:
            return False