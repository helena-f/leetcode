class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """


        # construct adjacency graph
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # using BFS
        queue = deque([source])
        visited = set([source])

        while queue:
            val = queue.popleft()
            if val == destination:
                return True
            for neighbor in graph[val]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
            
        return False