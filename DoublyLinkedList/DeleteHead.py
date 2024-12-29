'''
Delete Head of Doubly Linked List

Difficulty: Easy

Given a doubly linked list of size n, you have to delete the head of the linked list and return the new head.
Note: Please set the previous of new head to null, and set the next of old head to null, and then delete the old head.
'''
def deleteHead(head):
    cur=head.next
    head.next,head.prev=None,None
    cur.prev=None
    return cur