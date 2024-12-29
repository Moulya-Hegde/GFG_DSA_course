'''
Reverse a Doubly Linked List

Difficulty: Easy

Given a doubly linked list. Your task is to reverse the doubly linked list and return its head.
'''
class Solution:
    def reverseDLL(self, head):
        cur=head
        while cur.next!=None:
            temp=cur.next
            cur.next,cur.prev=cur.prev,cur.next
            cur=temp
        cur.next,cur.prev=cur.prev,None
        head=cur
        return head
        