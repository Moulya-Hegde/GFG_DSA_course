'''
Display Doubly Linked List

Difficulty: Basic

Given a doubly linked list of n elements. The task is to display the linked list.

Your task is to complete the given function displayList(), which takes head reference as argument and returns the doubly linked list as an array ( vector in cpp, ArrayList in java, list in python)
The driver's code print the list forward and backward.
'''

def displayList(head):
    res=[]
    cur=head
    while cur is not None:
        res.append(cur.data)
        cur=cur.next
    return res