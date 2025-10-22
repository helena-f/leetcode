"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        mp = {None : None}
        node = head
        while node:
            new = Node(node.val)
            mp[node] = new
            node = node.next
        
        node = head
        while node:
            new = mp[node]
            new.next = mp[node.next]
            new.random = mp[node.random]

            node = node.next

        return mp[head]