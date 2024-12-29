'''
Delete in a Doubly Linked List
Difficulty: Easy
Given a Doubly Linked list and a position. The task is to delete a node from a given position (position starts from 1) in a doubly linked list and return the head of the doubly Linked list.
'''
class Solution:
    def delete_node(self, head, x):
        count=1
        cur=head
        if x==1:
            cur=head.next
            head.next=None
            cur.prev=None
            head=cur
            return cur
        while count!=x:
            cur=cur.next
            count+=1
        if cur.next is None:
            cur.prev.next=None
            cur.prev=None
            return head
        cur.prev.next=cur.next
        cur.next.prev=cur.prev
        cur.next,cur.prev=None,None
        return head