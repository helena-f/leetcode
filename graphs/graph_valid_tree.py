class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # invalid if has cycle/backedge
        if n == 0:
            return True

        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)

        # print(graph)
        #     0
        #   /
        #   1
        # /  \   \ 
        # 2 - 3    4

        stack = [(0,-1)]
        visited = set()
        while stack:
            edge, parent = stack.pop()
            
            visited.add(edge)
            for nei in graph[edge]:
                if nei == parent:
                    continue
                if nei not in visited:
                    stack.append((nei, edge))
                else:
                    # print(edge, nei)
                    return False
        if len(visited) != n:
            return False
        return True
                    