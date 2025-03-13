# Reverse Linked List
# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

# Example 1:

# Input: head = [0,1,2,3]

# Output: [3,2,1,0]
# Example 2:

# Input: head = []

# Output: []

# Definition for singly-linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return None

#         newHead = head
#         if head.next:
#             newHead = self.reverseList(head.next)
#             head.next.next = head
#         head.next = None
        
#         return newHead
    
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
   
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None
    
    def insertAtBeginning(self, new_data):
        new_node = ListNode(new_data)  # Create a new node 
        new_node.next = self.head  # Next for new node becomes the   current head
        self.head = new_node  # Head now points to the new node

    def printList(self):
        temp = self.head # Start from the head of the list
        while temp:
            print(temp.data,end=' ') # Print the data in the current node
            temp = temp.next # Move to the next node
        print()  # Ensures the output is followed by a new line

    def reverseList(self):
        prev = None
        curr = self.head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev

if __name__ == '__main__':
    # Create a new LinkedList instance
    llist = LinkedList()

    llist.insertAtBeginning(0) 
    llist.insertAtBeginning(1) 
    llist.insertAtBeginning(2)  
    llist.insertAtBeginning(3)  
    llist.printList()
    llist.head = llist.reverseList()
    llist.printList()

