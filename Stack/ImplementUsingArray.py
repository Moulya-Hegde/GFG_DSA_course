'''
Implement Stack Using Array
Difficulty: Easy]
Implement stack using array

You are given q queries. The queries can be of 3 types:
Query Type:               Operation
               1 x:               Push x
                  2:               Pop the top element
                  3:               display stack from bottom to top in a single line.

The stack here is implemented by an array stack[], and maxSize of the stack is 100000. If a push operation is performed beyond this size, you must print "Stack Full"(without quotes) followed by a newline character ('\n'). Similarly, an unsuccessful pop operation should print "Stack Empty"(without quotes), followed by a newline character ('\n'). If a display operation is performed, print all elements of the stack in LIFO order, separated by spaces and on an empty stack print -1, followed by a newline character ('\n').

Example 1:

Input: q[] = {(1, 4), 3, 2, 2, 3}
Output: 4
        Stack Empty
        -1
Explanation: push() --> 4
display() --> 4 gets printed
pop() --> Pop 4
pop() --> stack is empty so print Stack 
          Empty
display() --> stack is empty so print -1

Example 2:

Input: q[] = {(1, 3), 3}
Output: 3
Explanation: push() --> 3
display() --> 3 gets printed
Your Task:
This is a function problem. The input task is performed by the driver code. You need to complete the provided functions. Complete function push() which takes an element as input parameter and pop(), display() functions.

Expected Time Complexity: push: O(1), pop: O(1), display: O(N)
Expected Auxilliary Space: O(N)

Constraints:
1 ≤ Number of Operations ≤ 103
'''
def push(data):
    global stackMax
    global top
    global stack
    top+=1

    if(top>=stackMax):
        top-=1
        print("Stack Full")
    else:
        stack[top]=data
      

def pop():
    global stack
    global stackMax
    global top
    if(top<=-1):
        print("Stack Empty")
    else:
        stack[top]=-1
        top-=1


        
        
def display():
    global stack
    global stackMax
    global top
    if(top<=-1):
        print(-1)
    else:
        i=0
        limit=top if top<stackMax else stackMax-1
        while(i<=top):
            print(stack[i],end=" ")
            i+=1
        print()
