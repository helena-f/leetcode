"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


        #133
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return
        # keep track of visited nodes
        visited = {}

       # copy the node and all its neighbors with dfs
        def dfs(currnode):
            if currnode in visited:
                return visited[currnode]
            copy = Node(currnode.val)
            visited[currnode] = copy
            
            for neighbor in currnode.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy
      
        return dfs(node)