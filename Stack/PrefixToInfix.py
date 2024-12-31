'''
Prefix to Infix Conversion
Difficulty: Medium
You are given a string S of size N that represents the prefix form of a valid mathematical expression. The string S contains only lowercase and uppercase alphabets as operands and the operators are +, -, *, /, %, and ^.Convert it to its infix form.
'''
class Solution:
    def preToInfix(self, pre_exp):
        stk=[]
        for i in reversed(pre_exp):
            if i.isalnum():
                stk.append(i)
            else:
                op1=stk.pop()
                op2=stk.pop()
                stk.append(f"({op1}{i}{op2})")
                
        return stk.pop()