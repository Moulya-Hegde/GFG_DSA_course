'''
Operations on Stack
Difficulty: Basic
Given a stack of integers and Q queries. The task is to perform the operation on stack according to the query.

The queries can be of 4 types:

i x: (adds element x in the stack).
r: (removes the topmost element from the stack).
h: Prints the topmost element.
f y: (check if the element y is present or not in the stack). Print "Yes" if present, else "No". 
'''
def insert(stack,x):
    stack.append(x)
    

#Function to remove top element from stack.
def remove(stack):
    if stack:
        stack.pop()
    
#Function to print the top element of stack.    
def headOf_Stack(stack):
    if stack:
        return stack[-1]
    
#Function to search an element in the stack.
def find(stack,x):
    if stack:
        return x in stack