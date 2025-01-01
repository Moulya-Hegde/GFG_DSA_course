'''
Operations on Queue
Difficulty: Basic
Given a queue of integers and Q queries. The task is to perform operations on queue according to the query. 

Queries are as:

i x : (adds element x in the queue from rear).

r : (Removes the front element of queue).

h : (Returns the front element).

f y : (check if the element y is present or not in the queue). Return "Yes" if present, else "No".
'''
class Solution:
    '''
    Function Arguments :
    		@param  : q (given list on which queue is implemented)
    		@param  : x (value to be used accordingly)
    		@return : None
    '''
    
    #Function to push an element in queue.
    def enqueue(self,q, x):
        q.append(x)
    
    #Function to remove front element from queue.
    def dequeue(self,q):
        if q:
            return q.pop(0)
        return -1
    
    #Function to find the front element of queue.
    def front(self,q):
        if q:
            return q[0]
        return -1
    
    #Function to find an element in the queue.
    def find(self,q, x):
        return x in q