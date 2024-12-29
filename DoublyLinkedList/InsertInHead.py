'''
Doubly Linked List Head Insert

Difficulty: Basic

Given a doubly linked list of size n, you need to insert an element data before the head and make it the new head.
'''
def insertInhead(head,data):
    temp=Node(data)
    head.prev=temp
    temp.next=head
    head=temp
    return head