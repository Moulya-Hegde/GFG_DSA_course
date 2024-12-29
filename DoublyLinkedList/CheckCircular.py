'''
Is The Doubly Linked List Circular

Difficulty: Easy

Given a doubly linked list, the task is to check if it is circular or not.

User Task:
The task is to complete the function isCircular() which takes head reference as an argument. The function should return true if the doubly LL is circular and false if it is not. (if the returned value if true, the driver code prints 1, otherwise 0)

'''
class Solution: 
    def isCircular(self, head):
        cur=head
        while cur.next!=head and cur.next is not None:
            cur=cur.next
        if cur.next==head:
            return True
        return False
