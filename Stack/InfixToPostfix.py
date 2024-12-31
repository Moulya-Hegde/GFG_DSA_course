'''
Infix to Postfix

Difficulty: Medium

Given an infix expression in the form of string s. Convert this infix expression to a postfix expression.

Infix expression: The expression of the form a op b. When an operator is in between every pair of operands.
Postfix expression: The expression of the form a b op. When an operator is followed for every pair of operands.
Note: The order of precedence is: ^ greater than * equals to / greater than + equals to -. Ignore the right associativity of ^.
'''
class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, s):
        store={"^":3,"*":2,"/":2,"+":1,"-":1}
        op=[]
        sym=[]
        for i in s:
            if i.isalnum():
                op.append(i)
            else:
                if i=='(':
                    sym.append(i)
                elif i==')':
                    while sym and sym[-1]!="(":
                        op.append(sym.pop())
                    sym.pop()
                else:
                    while sym and store.get(sym[-1],0)>=store.get(i,0):
                        op.append(sym.pop())
                    sym.append(i)
        while sym:
            op.append(sym.pop())
        return "".join(op)