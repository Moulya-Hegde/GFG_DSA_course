'''
Doubly Linked List Tail Insert

Difficulty: Basic

Given a doubly linked list of size n, you need to insert an element data after the tail.
'''
def insertInTail(head,data):
    temp=Node(data)
    cur=head
    while cur.next is not None:
        cur=cur.next
    cur.next=temp
    temp.prev=cur
    return head