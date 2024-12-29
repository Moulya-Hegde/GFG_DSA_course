'''
Compare Circular Doubly Linked Lists

Difficulty: Easy

Given two circular doubly linked lists of sizes n1 and n2 respectively, the task is check if the corresponding elements of the lists are same or not.
The tail of a circular doubly linked list is connected to head via its next pointer, and the previous pointer of head is connected to the tail.

Your Task:
The task is to complete the function compareCLL() which takes head1 and head2 references as an arguments. The function should return true if all the corresponding elements of the lists are same, else it should return false. (The driver's code print 1 if the returned value is true, otherwise false.)

Expected Time Complexity: O(n1 + n2).
Expected Auxiliary Space: O(1).
'''
class Solution:
    def compareCLL(self,head1,head2):
        cur1,cur2=head1,head2
        while cur1.next!=head1 and cur2.next!=head2:
            if cur1.data==cur2.data:
                cur1=cur1.next
                cur2=cur2.next
            else:
                return False
        if cur1.next==head1 and cur2.next==head2 and cur1.data==cur2.data:
            return True
        return False