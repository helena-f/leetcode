# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp = ListNode(0,head)
        second = temp
        first = head

        i = 0
        while i != n:
            first = first.next
            i+=1
        
        # find the N-nth position
        while first:
            first = first.next
            second = second.next

        # remove the pointer to the N-nth
        # pointer to the node after the one we want to remove
        
        second.next = second.next.next

        return temp.next




        