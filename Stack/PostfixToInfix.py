'''
Postfix to Infix Conversion
Difficulty: Medium
You are given a string that represents the postfix form of a valid mathematical expression. Convert it to its infix form.
'''

class Solution:
    def postToInfix(self, postfix):
        op=[]
        for i in postfix:
            if i.isalnum():
                op.append(i)
            else:
                op2=op.pop()
                op1=op.pop()
                op.append(f"({op1}{i}{op2})")
        return op.pop()
