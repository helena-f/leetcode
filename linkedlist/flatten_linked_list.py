"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        def recurse(head):
            curr = head
            tail = head
            while curr:
                old_next = curr.next
                if curr.child:
                    level_head, level_tail = recurse(curr.child)
                    curr.child = None

                    curr.next = level_head
                    level_head.prev = curr

                    if old_next:
                        level_tail.next = old_next
                        old_next.prev = level_tail
                    curr = level_tail
                    tail = level_tail
                else:
                    tail = curr
                    curr = curr.next
            return head, tail
        res, _ = recurse(head)
        return res

        