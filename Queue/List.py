'''
Queue Using Array

Difficulty: Basic

Implement a Queue using an Array. Queries in the Queue are of the following type:
(i) 1 x   (a query of this type means  pushing 'x' into the queue)
(ii) 2     (a query of this type means to pop an element from the queue and print the popped element. If the queue is empty then return -1)

We just have to implement the functions push and pop and the driver code will handle the output.
'''
class MyQueue:
    def __init__(self):
        self.l=[]
    #Function to push an element x in a queue.
    def push(self, x):
         self.l.append(x)
         
     
    #Function to pop an element from queue and return that element.
    def pop(self): 
        if self.l:
            res=self.l.pop(0)
            return res
        return -1
            