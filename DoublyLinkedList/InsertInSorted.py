'''
Insert in Sorted way in a Sorted DLL

Difficulty: Medium

Given a sorted doubly linked list and an element x, you need to insert the element x into the correct position in the sorted Doubly linked list(DLL).

Note: The DLL is sorted in ascending order
'''

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
'''
class Solution:
    # Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
        temp = Node(x)  # Create a new node with the given value
        cur = head      # Start from the head of the list

        # Case 1: Insert at the beginning if x is smaller than the head node's data
        if head.data >= x:
            temp.next = head
            head.prev = temp
            return temp  # Return the new head

        # Traverse the list to find the correct position for the new node
        while cur.next is not None and cur.data < x:
            cur = cur.next

        # Case 2: Insert at the end if x is greater than the last node's data
        if cur.next is None and cur.data < x:
            cur.next = temp
            temp.prev = cur
            return head

        # Case 3: Insert in the middle of the list
        temp.next = cur
        temp.prev = cur.prev
        if cur.prev:  # Ensure cur.prev is not None before accessing its next
            cur.prev.next = temp
        cur.prev = temp

        return head