class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        if not prerequisites:
            return True
        # dfs cycle detection
        for a, b in prerequisites:
            graph[b].append(a)
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            
            if graph[course] == []:
                return True

            visited.add(course)
            for nei in graph[course]:
                if not dfs(nei):
                    return False
            visited.remove(course)
            graph[course] = []
            return True
            

        for i in range(numCourses):
            if not dfs(i):
                return False
                
        return True

        # topological sort with bfs
        # initialize with degrees
        # decrease degree 
        # append nodes with indegree 0 to queue

        # bfs traverse
        # if degree == 0 add to queue

        # if num traversed equal to number courses, valid
        graph = defaultdict(list)
        indegrees = [0] * numCourses
        for a, b in prerequisites:
            graph[a].append(b)
            indegrees[b] += 1

        q = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        
        finished = 0
        while q:
            curr_course = q.popleft()
            finished += 1
            for nei in graph[curr_course]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
        
        return finished == numCourses
