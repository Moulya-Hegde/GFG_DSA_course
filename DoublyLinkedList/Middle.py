'''
Find Middle of Circular Doubly Linked List

Difficulty: Easy

Given a circular doubly linked list of odd size n, the task is to print the middle element.
The tail of a circular doubly linked list is connected to head via its next pointer, and the previous pointer of head is connected to the tail.

Your Task:
The task is to complete the function findMiddle() which takes head reference as an argument. The function should return the middle element of CDLL. 

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
'''
class Solution:
    def findMiddle(self, head):
        slow,fast=head,head
        while fast.next is not head:
            slow=slow.next
            fast=fast.next.next
        return slow.data