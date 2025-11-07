class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # directed graph
        # unweighted 
        # find valid path
        # use bfs
        # graph - i has all the nodes you can visit from i
        # keep results, current path array. 
        # start at node 0. if reach node n-1, 
        # add to path
        # need to find all possible paths

        n = len(graph) - 1
        res = []
        path = [0]
        def backtrack(i):
            if i == n:
                res.append(path[:])
                return
            
            for neighbor in graph[i]:
                path.append(neighbor)
                backtrack(neighbor)
                path.pop()

        backtrack(0)
        return res


        
        
