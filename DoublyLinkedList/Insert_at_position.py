'''
Doubly linked list Insertion at given position

Difficulty: Basic

Given a doubly-linked list, a position p, and an integer x. The task is to add a new node with value x at the position just after pth node in the doubly linked list and return the head of the updated list.
'''
# Your task is to complete this function
# function should add a new node after the pth position
# function shouldn't print or return any data

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''

class Solution:
    #Function to insert a new node at given position in doubly linked list.
    def addNode(self, head, p, x):
        temp=Node(x)
        cur=head
        count=0
        while count<p:
            cur=cur.next
            count+=1
        if cur.next==None:
            cur.next=temp
            temp.prev=cur
            return head
        temp.next=cur.next
        cur.next.prev=temp
        cur.next=temp
        temp.prev=cur
        return head
        