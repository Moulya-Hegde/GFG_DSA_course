'''
Queue using Linked List
Difficulty: Basic
Implement a Queue using Linked List. 
A Query Q is of 2 Types
(i) 1 x   (a query of this type means  pushing 'x' into the queue)
(ii) 2     (a query of this type means to pop an element from the queue and print the poped element)
'''
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    def __init__(self):
        self.front=self.rear=None
    #Function to push an element into the queue.
    def push(self, item):
        temp=Node(item)
        if self.front:
            self.rear.next=temp
        else:
            self.front=temp
        self.rear=temp
        
    
    #Function to pop front element from the queue.
    def pop(self):
        if self.front and self.front.next:
            res=self.front.data
        elif not self.front:
            return -1
        else:
            res=self.front.data
            self.rear=None
        self.front=self.front.next
        return res