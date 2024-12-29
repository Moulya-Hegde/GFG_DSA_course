'''
Delete Tail of Doubly Linked List
Difficulty: Easy
Given a doubly linked list of size n, you have to delete the tail (last element) in the linked list.
'''
def deleteTail(head):
    cur=head
    while cur.next is not None:
        cur=cur.next
    cur.prev.next=None
    cur.prev=None
    return head