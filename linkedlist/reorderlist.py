# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l, r = head, head.next

        while r and r.next:
            l = l.next
            r = r.next.next
        #l is now the midpoint
        
        #reverse l
        second = l.next
        prev = l.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first, second = head, prev
        while second:
            t1,t2 = first.next, second.next
            first.next = second
            second.next = t1
            first,second = t1, t2