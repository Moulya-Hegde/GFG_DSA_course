'''
Display Circular Doubly Linked List
Difficulty: Basic
Given a circular doubly linked list consisting of N nodes, the task is to print the elements from head to tail, then from tail to head in two separate lines.
The tail of a circular doubly linked list is connected to head via its next pointer, and the previous pointer of head is connected to the tail.

Your Task:
The task is to complete the function displayList() which takes head reference as an argument and return  the the circular doubly linked list as a list. 
Note: The returned list is printed twice, once forward and once backward.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
'''
def displayList(head):
    res=[]
    cur=head
    res.append(cur.data)
    cur=cur.next
    while cur!=head:
        res.append(cur.data)
        cur=cur.next
    return res